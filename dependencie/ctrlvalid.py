
from jose import JWTError, jwt,ExpiredSignatureError
from datetime import datetime, timedelta

from pydantic import JsonError
from config.conexiondb import conect
from config.setting import settingApi
from fastapi import Header, HTTPException

from ast import literal_eval

SECRET_KEY = "f1a3920f167b245ffb1e32d3c1cf9557bfc84d4399965ff7fbf80fc0e5d9e98d"
ALGORITHM = "HS256"

def very_keycode_regi(code:dict):
    print(conect.getDb().keycode.count_documents(code))
    if conect.getDb().keycode.count_documents(code) == 1:
        datax = conect.getDb().keycode.find_one(code,{'_id':0,'status':1})
        print(datax,'que paso')
        if datax['status']:
            return True
        else:
            return False
    else:
        return False
def very_user_regi(userx:dict):
    if conect.getDb().user.count_documents(userx) == 1:
        return False
    else:
        return True

class validTok:
    token:str


def validPlanGlobal(token):
    dataus = get_data_token_valid(token)
    tokenPlan = conect().getDb().user.find_one({'username':dataus['username']},{'_id':0,'planToken':1,'creditos':1})       
    return {'dataPlan':get_data_token_valid(tokenPlan['planToken']),'creditos':tokenPlan['creditos'],'username':dataus['username']}
  

def validPlanUS(email:str):
    tokenPlan = conect().getDb().user.find_one({'email':email},{'_id':0,'planToken':1,'creditos':1})    
    return {'dataPlan':get_data_token_valid(tokenPlan['planToken']),'creditos':tokenPlan['creditos']}




def validPlanAdmin(chkbylorus:str= Header(...)):
    dataus = get_data_token_valid(chkbylorus)
    tokenPlan = conect().getDb().user.find_one({'username':dataus['username']},{'_id':0,'planToken':1})
    if get_data_token_valid(tokenPlan['planToken'])['plan'] == "Administrador":
        pass
    else:
        raise HTTPException(status_code=401, detail="Muy bien pensado ahora vayase ...")
  


def get_data_token_valid(chkbylorus:str= Header(...)):
    token =chkbylorus
  
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return literal_eval(payload.get('sub')) 
    except ExpiredSignatureError as e:
        print("session",e)
        raise HTTPException(status_code=401, detail="Credencial invalid rufian ¬¬")
    except JWTError as e:
        print("error en jwt general",e)
        raise HTTPException(status_code=400, detail="error contactar admin")
    except Exception as e:
        print("aqui hay un error tok")
        raise HTTPException(status_code=400, detail="error contactar admin")




def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


