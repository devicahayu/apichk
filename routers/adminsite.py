from fastapi import APIRouter, Depends, HTTPException,Body,Header
from config.conexiondb import conect
from control.controler_admin import ctrAdmin
from control.controler_site import controlSite
from pydantic import BaseModel, Field
from dependencie.ctrlvalid import validPlanAdmin


siteCtrAdmin = APIRouter(
    tags=["site_control_admin"],
    prefix="/api/admin/site",
    dependencies=[Depends(validPlanAdmin)]
)



class dataSettingKeys(BaseModel):
    days:int = Field(...)
    credit:int = Field(...)
    plan:str = Field()
    count:int = Field(...)

class proxyDataCore(BaseModel):
    proxy:str = Field(...)



@siteCtrAdmin.post("/upSocklivexx")
def getscraper(ctradminx:ctrAdmin = Depends(),chkbylorus:str= Header(...),dataproxy:proxyDataCore = Body(...)):
    return ctradminx.upsocks(dataproxy.proxy)


@siteCtrAdmin.post("/deletesocksxx")
def getscraper(ctradminx:ctrAdmin = Depends(),chkbylorus:str= Header(...)):
    return ctradminx.deleteSock()




@siteCtrAdmin.post("/create_keys")
def getscraper(ctradminx:ctrAdmin = Depends(),chkbylorus:str= Header(...), dataKey:dataSettingKeys = Body(...)):
    return ctradminx.createKeys(dataKey)



