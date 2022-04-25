from fastapi import APIRouter, Depends, HTTPException,Body,Header
from control.controler_user import controler_user

from dependencie.ctrlvalid import get_data_token_valid

router_userctr = APIRouter(
    prefix='/api/user',
    tags=['control_user'],
    dependencies=[Depends(get_data_token_valid)]
)




@router_userctr.post("/get/autosave")
def DataAuto(getAuto:controler_user = Depends(),chkbylorus:str= Header(...)):
    return getAuto.getAutoSAve(chkbylorus)
    