from fastapi import APIRouter, Depends, HTTPException,Body,Header
from config.conexiondb import conect

from control.controler_site import controlSite
from pydantic import BaseModel, Field


siteCtrV1 = APIRouter(
    tags=["site_control_apiv1"],
    prefix="/api/sitev1"
)

@siteCtrV1.post("/getsock1")
def getscraper(ctrsitev1:controlSite = Depends(),chkbylorus:str= Header(...)):
    return ctrsitev1.getDataSokc()
@siteCtrV1.get("/getsock2")
def getscraper(ctrsitev1:controlSite = Depends()):
    return ctrsitev1.getDataSokc()
