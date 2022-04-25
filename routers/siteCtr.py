from fastapi import APIRouter, Depends, HTTPException,Body,Header
from control.controler_site import controlSite

from dependencie.ctrlvalid import get_data_token_valid


siteCtr = APIRouter(
    tags=["site_control"],
    prefix="/api/ctr/site",
    dependencies=[Depends(get_data_token_valid)]
)


@siteCtr.post('/getData')
def siteData(ctrsite:controlSite = Depends(),chkbylorus:str= Header(...)):
    dataSite = ctrsite.getDataInitSite(chkbylorus)
    
    return dataSite

