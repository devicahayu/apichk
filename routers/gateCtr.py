
from fastapi import APIRouter, Header, Body,Depends
from pydantic import BaseModel, Field
from dependencie.ctrlvalid import get_data_token_valid
from control.controler_gate import ctrGate
from typing import Optional



routerGate = APIRouter(
    prefix='/api/gatectr',
    tags=['gatectr'],
    dependencies=[Depends(get_data_token_valid)]
)


class gateDataCore(BaseModel):
    cc:str = Field(...)
    proxy:str = Field(...)
    namegate:str = Field()
    timeout:str = Field(...)
    ext:Optional[str] = None
    
@routerGate.post('/run_gate')
def coreGate(gateContent:ctrGate = Depends(),dataGate:gateDataCore = Body(...) ,chkbylorus:str= Header(...)):
    dataGate = gateContent.confiCard(datax=dataGate,token=chkbylorus)
    return dataGate