from fastapi import FastAPI, Depends,WebSocket
from fastapi.middleware.cors import CORSMiddleware
from routers import autenticacion_user,siteCtr,site_ws, gateCtr,adminsite,sitev1,controluser
from dependencie.ctrlvalid import get_data_token_valid
app = FastAPI()

origins = [
    "http://localhost:4200"
]
#"http://localhost:4200"
#https://pro-checker.com
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(autenticacion_user.router)
app.include_router(siteCtr.siteCtr)
app.include_router(gateCtr.routerGate)
app.include_router(site_ws.ws)
app.include_router(sitev1.siteCtrV1)
app.include_router(controluser.router_userctr)

app.include_router(adminsite.siteCtrAdmin)

