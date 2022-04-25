
from fastapi import APIRouter, Body, Depends
from pydantic.networks import EmailStr
from fastapi.security import OAuth2PasswordRequestForm

from werkzeug.local import LocalProxy
#base de datos
from config.conexiondb import conect

from passlib.context import CryptContext
from pydantic import BaseModel, Field

from datetime import datetime, timedelta

#dependecias
from dependencie.ctrlvalid import create_access_token, very_keycode_regi, very_user_regi


from time import sleep
from random import randint

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)



# modelos de auth 
class user_register(BaseModel):
    username:str = Field(...,min_length=3,max_length=50)
    password:str = Field(...,min_length=5,max_length=50)
    keycode:str = Field(...,min_length=49,max_length=49)

class response_peticion_user():
    code:int
    msg:str


# funciones propias de auth
def very_hash_password(pwd:str,username:str) -> bool:
    hash_password_user = conect.getDb().user.find_one({'username':username},{'password':1,'_id':0})

    if not pwd_context.verify(pwd, hash_password_user):
        return False
    else:
        return True

def hash_password(pwd:str) -> str:
    return pwd_context.hash(pwd)



# metodos de auth
def create_reg_user(data:user_register) -> bool:
    plan = conect.getDb().keycode.find_one({'keycode':data.keycode},{'plan':1,'_id':0})

    if plan['plan'] == 'Ligth':
        timeplan = {'time':timedelta(minutes=21600),'creditos':1200,'plan':plan['plan']}
    elif plan['plan'] == 'Premiun':
        timeplan = {'time':timedelta(minutes=43200),'creditos':2500,'plan':plan['plan']}
    elif plan['plan'] == 'Diamond':
        timeplan = {'time':timedelta(minutes=86400),'creditos':5500,'plan':plan['plan']}
    elif plan['plan'] == 'Administrador':
        timeplan = {'time':timedelta(minutes=527040),'creditos':5000,'plan':plan['plan']}

    timeDa:datetime =datetime.utcnow()+ timeplan['time']

     
    tokenData = create_access_token({'sub':str({'plan':plan['plan'],'time':timeDa.strftime('%d/%m/%Y %H:%M:%S'),'user_email':data.email})},expires_delta=timeplan['time'])
    timeplan['planToken'] = tokenData
    timeplan['password'] = hash_password(data.password)
    del timeplan['time']

    userdata = dict(data) | timeplan
    idx= conect.getDb().user.insert_one(userdata).inserted_id
    if conect.getDb().user.count_documents({'_id':idx}) == 1:
        conect.getDb().keycode.update_one({'keycode':data.keycode},{'$set':{'status':False,'used':data.username}})
        return True
    else:
        return False

def very_reg(data:user_register) -> response_peticion_user:
    #verificar si la key que nos envian son correctas
    if very_keycode_regi({'keycode':data.keycode}):
        if very_user_regi({'username':data.username}):
            if very_user_regi({'email':data.email}):
                if create_reg_user(data):
                    # crear el login
                    token = create_access_token({'sub':str({'email':data.email,'username':data.username})},expires_delta=timedelta(minutes=2880))
                    status = {'code':2,'msg':token}
                else:
                    status = {'code':5,'msg':'Error en crear usuario'}
            else:
                status = {'code':4,'msg':'El email ya existe '}
        else:
            status = {'code':3,'msg':'El usuario existe '}
    else:
        status = {'code':1,'msg':'No existe el keycode'}
    
    return status


def access_login(username:str,pwd:str) -> response_peticion_user:
     # verificar si el usuario administrado existe
    user = conect.getDb().user.find_one({'username':username},{'_id':0,'password':1,'email':1,'plan':1})
    if user != None:
        if not pwd_context.verify(pwd,user['password']):
            return {'code':1,'msg':'user or password incorrect'}
        else:
            #creacion de token de acceso
            token = create_access_token({"sub":str({"username":username}),'apiv2':username},expires_delta=timedelta(minutes=2880))
            return {'code':2,'msg':token,'plan':user['plan']}
    else:
        return {'code':1,'msg':'user or password incorrect'}


# Rutas
@router.post('/register')
def register_user(reg:user_register = Body(...)):

    status = None
    if conect.getDb().user.count_documents({'username':reg.username}) == 0:
        keyx = conect.getDb().keycode.find_one({'keycode':reg.keycode},{'plan':1,'credit':1,'time':1,'status':1,'_id':0})
        if keyx != None:
            if keyx['status']:
                if keyx['plan'] == 'Light':
                    timeplan = {'time':timedelta(days=keyx['time']),'creditos':keyx['credit'],'plan':keyx['plan']}
                elif keyx['plan'] == 'Premiun':
                    timeplan = {'time':timedelta(days=keyx['time']),'creditos':keyx['credit'],'plan':keyx['plan']}
                elif keyx['plan'] == 'Diamond':
                    timeplan = {'time':timedelta(days=keyx['time']),'creditos':keyx['credit'],'plan':keyx['plan']}
                elif keyx['plan'] == 'Administrador':
                    timeplan = {'time':timedelta(days=keyx['time']),'creditos':keyx['credit'],'plan':keyx['plan']}
                elif keyx['plan'] == 'Personalizado':
                    timeplan = {'time':timedelta(hours=keyx['time']),'creditos':keyx['credit'],'plan':keyx['plan']}

                timeDa:datetime =datetime.utcnow()+ timeplan['time']
                
                tokenData = create_access_token({'sub':str({'plan':keyx['plan'],'time':timeDa.strftime('%d/%m/%Y %H:%M:%S'),'user':reg.username})},expires_delta=timeplan['time'])
                timeplan['planToken'] = tokenData
                timeplan['password'] = hash_password(reg.password)
                del timeplan['time']

                userdata = dict(reg) 

                userdata.update(timeplan)
                statux = conect.getDb().keycode.find_one({'keycode':reg.keycode},{'status':1})
                
                if statux['status']:
                    conect.getDb().keycode.update_one({'keycode':reg.keycode},{'$set':{'status':False,'used':reg.username}})
                    conect.getDb().user.insert_one(userdata)
  
                    token = create_access_token({'sub':str({'username':reg.username})},expires_delta=timedelta(minutes=2880))
                    status = {'code':2,'msg':token}           

                else:
                    status = {'code':3,'msg':'El usuario existe -_-'}
                
                
            else:
                status = {'code':1,'msg':'Keycode registrado'}
            
        else:
            status = {'code':1,'msg':'No existe el keycode'}
        
    else:
        status = {'code':3,'msg':'El usuario existe '}
        
    return status
        

@router.post('/login')
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    return access_login(username=form_data.username,pwd=form_data.password)



