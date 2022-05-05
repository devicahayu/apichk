from shutil import ExecError
from config.conexiondb import conect
from dependencie.ctrlvalid import validPlanGlobal
from model.models import autosaveCC
import requests
from datetime import datetime
from hashlib import md5




class controler_user:
    def createAutosave(self,dataG,user:str):
        vakue =md5(bytes(user,'utf-8')).hexdigest()

        idTem = 'teamid-'+vakue+'-autosave'
        datax = requests
        binx = dataG['cc'][0:6]

        x = datax.get("https://lookup.binlist.net/"+binx)
        try:

            timexs =datetime.utcnow().timestamp()
            scheme =x.json()['scheme']
            typex =x.json()['type']
            brand =x.json()['brand']
            countryx = x.json()['country']['alpha2']
            bank =x.json()['bank']['name']
            

            conect.getDb().autosave.insert_one({'cc':dataG['cc'],'gate':dataG['gate'],'idUser':idTem,'scheme':scheme,'type':typex,'bank':bank,'brand':brand,'country':countryx,'time':timexs})
            
        except KeyError as e:
            if str(e) == "'name'":
                conect.getDb().autosave.insert_one({'cc':dataG['cc'],'gate':dataG['gate'],'idUser':idTem,'scheme':scheme,'type':typex,'brand':brand,'country':countryx,'bank':None,'time':timexs})
            else:
                conect.getDb().autosave.insert_one({'cc':dataG['cc'],'gate':dataG['gate'],'idUser':idTem,'scheme':None,'type':None,'brand':None,'country':None,'bank':None,'time':timexs})    
        
    def getAutoSAve(self,token):


        try:
            userData =  validPlanGlobal(token)
            vakue = md5(bytes(userData['username'],'utf-8')).hexdigest()
            idTem = 'teamid-'+vakue+'-autosave'
            datax = list(conect.getDb().autosave.find({'idUser':idTem},{'_id':0,'idUser':0}))
            return {'code':2,'autosave':datax}
        except Exception as e:
            return {'code':1}
        
        
