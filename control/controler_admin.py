
from config.conexiondb import conect
from model.models import keyCreate
import string
import random

class ctrAdmin:
    def upsocks(self,proxy):
        conect.getDb().proxyScraper.insert_one({'proxy':proxy})
        return {'code':2,'data':'sucess scraper proxy','proxy':proxy}

    def deleteSock(self):
        conect.getDb().proxyScraper.delete_many({})
        return {'code':2,'data':'sucess delete proxy'}

    def createKeys(self,datakeys:keyCreate):

        number_of_strings = datakeys.count
        length_of_string = 10
        keysx = list()
        try:
            for x in range(number_of_strings):
                block1 =''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                block2 =''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                block3 =''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                keys = f'MULTIPROCHK-CODE-{block1}-{block2}-{block3}'
                datakeysGEt = {'keycode':keys,'status':True,'used':None,'plan':datakeys.plan,'time':datakeys.days,'credit':datakeys.credit}
                conect.getDb().keycode.insert_one({'keycode':keys,'status':True,'used':None,'plan':datakeys.plan,'time':datakeys.days,'credit':datakeys.credit})
                keysx.append(datakeysGEt)
            return {'code':2,'datakeys':keysx}
        except Exception as e:
            return {'code':1}

        

