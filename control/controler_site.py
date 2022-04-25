#base de datos
from time import time
from config.conexiondb import conect
from dependencie.ctrlvalid import  validPlanGlobal
from datetime import datetime

from hashlib import md5


class controlSite:
    def getDataInitSite(self,token):
        userData =  validPlanGlobal(token)
        TimeFaltante = datetime.strptime(userData["dataPlan"]["time"],'%d/%m/%Y %H:%M:%S').timestamp()- time()
        
        vakue =md5(bytes(userData['username'],'utf-8')).hexdigest()

        idTem = 'teamid-'+vakue+'-autosave'
        
        datalive = conect.getDb().autosave.count_documents({'idUser':idTem})
        
        home = {'creditos':userData["creditos"],'plan':userData["dataPlan"]['plan'],'time':TimeFaltante}
        dataGateList = list(conect.getDb().gatecore.find({},{'_id':0,'userPrivate':0}))
        
        gen = list()
        cards = list()
        vip = list()
        private = list()
        account = list()

        for gate in dataGateList:
            if gate['typeGate'] == 'generadas':
                gen.append(gate)
            elif gate['typeGate'] == 'cards':
                cards.append(gate)
            elif gate['typeGate'] == 'vip':
                vip.append(gate)
            elif gate['typeGate'] == 'private':
                private.append(gate)
            elif gate['typeGate'] == 'account':
                account.append(gate)

    
        return {'code':2,'gateList':{'Generadas':gen,'Cards':cards,'Vip':vip,'private':private,'account':account,'statusCarga': True},'homeinfo':{'homedata':home,'liveTotalUSr':datalive,'statusCarga':True}} 

    def getDataSokc(self):
        
        dataSocks = list(conect.getDb().proxyScraper.find({},{"_id":0,"proxy":1}))

        dataxS= list()
        for datax in dataSocks:
            dataxS.append(datax['proxy'])
        return {'code':2,"sock":dataxS,'data':"success data"}