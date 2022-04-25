from importlib import import_module
from dependencie.infocc import info
from dependencie.infobill import infobill
from random import randint
import datetime

from dependencie.ctrlvalid import validPlanGlobal
from fastapi import  HTTPException

from control.controler_user import controler_user
from model.models import gateData,autosaveCC

from config.conexiondb import conect


from time import sleep

class ctrGate:
    def __init__(self):
        self.infoxcc = info()
        self.nameGate = None
        self.typeExp:str = "xx xxxx"
        self.__objmogate = None
        
    def descuentoLive(self,dataUSC,codeR,datAGate):

        sleep(randint(0,4))
        dataCRedit = conect.getDb().user.find_one({'username':dataUSC['username']},{'_id':0,'creditos':1})
        if codeR == 2:
            creditActual = dataCRedit['creditos'] - datAGate['live']
        elif codeR ==1:
            creditActual = dataCRedit['creditos'] - datAGate['dead']
        conect.getDb().user.update_one({'username':dataUSC['username']}, {"$set":{'creditos':creditActual}})
        return creditActual

    def validPlanGate(self,token):
        dataus = validPlanGlobal(token) #email credits username plan
        # futura validacion para el uso de gates segun el plan...
        if dataus['creditos'] < 5:
            raise HTTPException(status_code=403, detail="plan invalido o insuficiente en creditos")
        return dataus

    def __configGate(self, nameGate:str,typeExp:str):
        #area temporal
        self.nameGate =nameGate
        self.typeExp = typeExp
        self.__objmogate = import_module('core_gateway.gates.'+self.nameGate)

    def confiCard(self,datax:gateData,token):
        #aqui va venir la area para extraer los descuentos
        datAGate = conect.getDb().gatecore.find_one({'nameGate':datax.namegate},{'_id':0,'live':1,'dead':1,'typeExp':1,'process':1})
        
        processActual = datAGate['process'] +1
        
        conect.getDb().gatecore.update_one({'nameGate':datax.namegate}, {"$set":{"process":processActual}})
        
        dataUSC = self.validPlanGate(token)
        
        self.__configGate(datax.namegate,datAGate['typeExp']) 
        try:
            settingAuto = controler_user()
            
            # formateo de la cc a ocupar en los gates
            self.infoxcc.info(datax.cc,self.typeExp)

            if self.__validexp(datax.cc):
                responsxr = self.__objmogate.CoreGateCode(self.infoxcc.brand)
                
                dataResponse = responsxr.processCodeGate(self.infoxcc,datax)
                if dataResponse == None:
                    return {'msg':4,'contentCC':datax.cc,'proxy':datax.proxy}
                
                #descuento
                if dataResponse['msg'] == 1 or dataResponse['msg'] == 2:
                    dataResponse['credits'] = self.descuentoLive(dataUSC,dataResponse['msg'],datAGate)    

                if dataResponse['msg'] == 2:
                    autosavelive = {'gate':datax.namegate,'cc':datax.cc}
                    liveCount = conect.getDb().gatecore.find_one({'nameGate':datax.namegate},{'_id':0,'countLive':1})
                    liveActual = liveCount['countLive'] +1
                    conect.getDb().gatecore.update_one({"nameGate":datax.namegate}, {"$set":{"countLive":liveActual}})
                    settingAuto.createAutosave(autosavelive,dataUSC['username'])
                    
                
                return dataResponse
            
            else:
                return {'msg':3,'ccResponse':'Expired card => '+datax.cc, 'contentCC': datax.cc,'datext':'teamsmilerxsas@hotmail.com','proxy':datax.proxy}
        except Exception as e:
            # hay que mejorar las excepciones
            print('error en valid card: ', e)
            return {'msg':3,'contentCC':datax.cc,'ccResponse': 'ERROR NO CAPTURADO...','datext':'teamsmilerxsas@hotmail.com','proxy':datax.proxy}
        
    def __validexp(self,cc:str) -> bool:
        valid = info()
        valid.info(cc,'x xxxx')

        if int(valid.expm) < datetime.datetime.now().month and int(valid.expy) == datetime.datetime.now().year or int(valid.expy) < datetime.datetime.now().year:
            return False
        else:
            return True
        
