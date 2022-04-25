from asyncio.proactor_events import constants
from fastapi import APIRouter, WebSocket,WebSocketDisconnect, Query, status
from control.controler_ws import ConnectionManager

ws = APIRouter()

manager = ConnectionManager()

@ws.websocket("/api/ws/site")
async def ws_ctr_site(websocket: WebSocket,token = Query(None)):
    
    #validacion de credenciales
    dataAuth = await manager.validAuth(token=token)
    if dataAuth['status']:
        await manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_json()
                xcliente = data['msgCliente']
                #primera conexion
                if xcliente['type'] == 'connect':
                    await manager.very_add_user(dataAuth['data']['username'],websocket)
                    await manager.send_personal_message(({"typeAction":"active","data":await manager.get_active_user()}), websocket)
                elif xcliente['type'] == 'desconectar':
                    await manager.disconnect(websocket,True)
                    print('usuario desconectado Globalmente')
  
        except WebSocketDisconnect:
            await manager.disconnect(websocket,False)
            print('usuario desconectado')
    else:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        print('Desconexion por violacion de autenticacion')
            

