from fastapi import WebSocket
from typing import List, Dict
from jose import JWTError, jwt
from ast import literal_eval


SECRET_KEY = "f1a3920f167b245ffb1e32d3c1cf9557bfc84d4399965ff7fbf80fc0e5d9e98d"
ALGORITHM = "HS256"

class conecctionUser:
    username:str
    websocket:List[WebSocket]

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.active_connections_users:List[conecctionUser] = []

    async def validAuth(self,token:str):
        try:
            #validacion de session
            payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
            return {'status':True,'data':literal_eval(payload.get('sub'))} 
        except JWTError as e:
            return {'status':False,'data':None}
        
    async def very_add_user(self,user:str, websocket:WebSocket):
        #verificar si el usuario ya esta registrado en la cola de conexion
        
        if len(self.active_connections_users) > 0:
            dataUSAct = self.active_connections_users
            indexusAc =0 
            
            while len(self.active_connections_users) > indexusAc:
                if self.active_connections_users[indexusAc].username == user:
                    statusConexion:bool = False
                    
                    for conex in self.active_connections_users[indexusAc].websocket:
                        if conex == websocket:
                            statusConexion = True
                            break
                        
                    if not statusConexion:
                        self.active_connections_users[indexusAc].websocket.append(websocket)
                        break
                indexusAc +=1
            else:
                print('nuevo usuario')
                datax1 = conecctionUser()
                datax1.username =user
                datax1.websocket  = [websocket]
                self.active_connections_users.append(datax1)
                
                await self.broadcast('active')
        else:
            datax = conecctionUser()
            datax.username = user
            datax.websocket =[websocket]  
            self.active_connections_users.append(datax)
            #notificar del nuevo usuario activo
            await self.broadcast('active')

    async def get_active_user(self) -> List[str]:
        userActive:List[str] = []
        for activeUSer in self.active_connections_users:
            userActive.append(activeUSer.username)
        return userActive
    
    async def active_user(self) -> None:
        userActive:List[str] = await self.get_active_user()
        for conect in self.active_connections:
            await conect.send_json({"typeAction":"active","data":userActive})
        
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket,globalConnect:bool):
        try:
            self.active_connections.remove(websocket)
        except:
            print('error',self.active_connections,websocket)
        
        #desconexion de usuario en sus websocket
        for i,userConex in enumerate(self.active_connections_users):
            indextweb = 0
            while len(userConex.websocket) > indextweb:
                if userConex.websocket[indextweb] == websocket:
                    self.active_connections_users[i].websocket.remove(websocket)
                    if len(self.active_connections_users[i].websocket) == 0 or globalConnect:
                        if globalConnect:
                            for webcon  in self.active_connections_users[i].websocket:
                                #self.active_connections.remove(webcon)
                                await webcon.close(code=status.WS_1008_POLICY_VIOLATION)
                        self.active_connections_users.remove(self.active_connections_users[i])
                        
                        await self.broadcast('active')
                    break
                indextweb +=1
            else:
                print('cambio de user')


    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)
        
    async def broadcast(self, action: str):
        if action  == 'active':
            await self.active_user()
            