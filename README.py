#for letter in 'Nghia': 
   #if letter == 'a':
      #pass
      #('Day la khoi pass')
   #print('Chu cai hien tai :', letter)

#print("Good bye!")
from time import sleep
import base64
import warnings,threading
from six.moves.urllib_parse import urljoin
import os,json,requests,string, base64, six
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import unquote
from anycaptcha import *
import requests
from selenium import webdriver
import requests
from urllib.parse import unquote
from selenium.webdriver.common.by import By
from time import sleep
x=0 
y=0
apikey=input("Api Key Anycaptcha: ")
user=input("User-Agent: ")
cookie_fb=input("Coookie Facebook: ")
url=input("Link Machine-Liker: ")
link=input("Link Rpw-liker: ")
dataid=requests.post('https://id.traodoisub.com/api.php',data={
  "link":link
})
idtds=dataid.json()["id"]
def getmch():
  cài_đặt_web3=webdriver.ChromeOptions()
  cài_đặt_web3.add_argument('--lang=en')
  cài_đặt_web2=cài_đặt_web3
  cài_đặt_web=cài_đặt_web2
  cài_đặt_web.add_experimental_option('excludeSwitches', ['enable-logging'])
  cài_đặt_web22=cài_đặt_web
  cài_đặt_web22.add_argument("--window-size=580,800")
  cài_đặt_web22.add_argument(f"user-agent={user}")
  cài_đặt_web22.add_experimental_option('useAutomationExtension', False)
  cài_đặt_web22.add_argument('--disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options=cài_đặt_web22)
  driver.set_window_position(0, 0)
  driver.get('https://www.machine-liker.com/login/');sleep(2)
  driver.execute_script("""window.open('https://www.machine-liker.com/login/')""")
  sleep(12)
  driver.refresh()
  sleep(2)
  code = driver.page_source.split('id="user-code" value="')[1].split('"')[0]
  headers = {
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'save-data': 'on',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'none',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cookie': cookie_fb
                        }
  check_dv = requests.get(f'https://mbasic.facebook.com/device?user_code={code}', headers=headers).text
  fb_dtsg = check_dv.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
  jazoest = check_dv.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
  qr = check_dv.split('name="qr" value="')[1].split('"')[0]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'upgrade-insecure-requests': '1',
                            'origin': 'https://mbasic.facebook.com',
                            'content-type': 'application/x-www-form-urlencoded',
                            'save-data': 'on',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'qr': qr,
                            'user_code': code
                        }
  url_c = requests.post('https://mbasic.facebook.com/device/redirect/', headers=headers, data=data).url
  url_f = unquote(url_c).split('&next=')[1]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'save-data': 'on',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  find_data = requests.get(url_f, headers=headers).text
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
  scope = find_data.split('name="scope" value="')[1].split('"')[0]
  jazoest = find_data.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
  logger_id = find_data.split('name="logger_id" value="')[1].split('"')[0]
  user_code = find_data.split('name="user_code" value="')[1].split('"')[0]
  encrypted_post_body = find_data.split('name="encrypted_post_body" value="')[1].split('"')[0]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'origin': 'https://mbasic.facebook.com',
                            'upgrade-insecure-requests': '1',
                            'content-type': 'application/x-www-form-urlencoded',
                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                            'referer': url_f,
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'from_post': '1',
                            'deduplicate': '',
                            'link_customer_account': '',
                            'read': '',
                            'link_news_subscription': '',
                            'write': '',
                            'extended': '',
                            'confirm': '',
                            'reauthorize': '',
                            'user_messenger_contact': '',
                            'seen_scopes': '',
                            'response_type': 'code',
                            'auth_type': 'rerequest',
                            'auth_nonce': '',
                            'calling_package_key': '',
                            'default_audience': '',
                            'dialog_type': 'gdp_v4',
                            'fbapp_pres': '',
                            'ret': '',
                            'return_format': 'code',
                            'domain': '',
                            'scope': scope,
                            'sso_device': '',
                            'logger_id': logger_id,
                            'sheet_name': 'initial',
                            'fallback_redirect_uri': '',
                            'sdk': '',
                            'facebook_sdk_version': '',
                            'sdk_version': '',
                            'user_code': user_code,
                            'logged_out_behavior': '',
                            'install_nonce': '',
                            'l_nonce': '',
                            'original_redirect_uri': '',
                            'loyalty_program_id': '',
                            'messenger_page_id': '',
                            'reset_messenger_state': '',
                            'aid': '',
                            'deferred_redirect_uri': '',
                            'code_redirect_uri': '',
                            'extras': '',
                            'tp': 'unspecified',
                            'fx_app': '',
                            'is_promote_auth': '',
                            'encrypted_post_body': encrypted_post_body,
                            'cbt': '',
                            '__CONFIRM__': 'Tiếp+tục'
                        }
  do = requests.post('https://mbasic.facebook.com/v2.0/dialog/oauth/confirm/', headers=headers, data=data)
  url_z = unquote(do.url).split('next=')[1]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'save-data': 'on',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'none',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  don = requests.get(url_z, headers=headers).text
  sleep(7)
  driver.execute_script("""document.querySelector('[data-action="verify-login"]').click()""");sleep(8)
  ckkk = []
  lis_ck = []
  for x in driver.get_cookies():
    ckkk.append(x['name']+"="+x['value'])
  ck = ';'.join(ckkk)+';'
  lis_ck.append(ck)
  cokiemcn = lis_ck[0]
  headersa = {

        'user-agent': user,
        'cookie': cokiemcn
                        }
  gétitekey= requests.get('https://www.machine-liker.com/verify/',headers=headersa).text

  sitekey_2 = gétitekey.split('data-sitekey="')[1].split('"')[0]
  driver.quit()
  print("Đang Tiến Hành Vượt Captcha",end='\r')
  datacaptcha = giaicaptcha('https://www.machine-liker.com/verify/', sitekey_2, apikey)
  print("Vượt Captcha Thành Công....",end='\r')
  datavuotcap = {
        'g-recaptcha-response': datacaptcha
        }
  giaicapt = requests.post('https://www.machine-liker.com/verify/',data=datavuotcap,headers=headersa)
  sleep(5)
  driver.quit()
  return cokiemcn
def getrpw():
  cài_đặt_web3=webdriver.ChromeOptions()
  cài_đặt_web3.add_argument('--lang=en')
  cài_đặt_web2=cài_đặt_web3
  cài_đặt_web=cài_đặt_web2
  cài_đặt_web.add_experimental_option('excludeSwitches', ['enable-logging'])
  cài_đặt_web22=cài_đặt_web
  cài_đặt_web22.add_argument("--window-size=580,800")
  cài_đặt_web22.add_argument(f"user-agent={user}")
  cài_đặt_web22.add_experimental_option('useAutomationExtension', False)
  cài_đặt_web22.add_argument('--disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options=cài_đặt_web22)
  driver.set_window_position(0, 0)
  driver.get('https://rpwliker.com')
  sleep(5)
  code=driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div/div/div[2]/div/input').get_attribute("value")
  headers = {
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'save-data': 'on',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'none',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cookie': cookie_fb
                        }
  check_dv = requests.get(f'https://mbasic.facebook.com/device?user_code={code}', headers=headers).text
  fb_dtsg = check_dv.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
  jazoest = check_dv.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
  qr = check_dv.split('name="qr" value="')[1].split('"')[0]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'upgrade-insecure-requests': '1',
                            'origin': 'https://mbasic.facebook.com',
                            'content-type': 'application/x-www-form-urlencoded',
                            'save-data': 'on',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'qr': qr,
                            'user_code': code
                        }
  url_c = requests.post('https://mbasic.facebook.com/device/redirect/', headers=headers, data=data).url
  url_f = unquote(url_c).split('&next=')[1]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'save-data': 'on',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  find_data = requests.get(url_f, headers=headers).text
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
  scope = find_data.split('name="scope" value="')[1].split('"')[0]
  jazoest = find_data.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
  logger_id = find_data.split('name="logger_id" value="')[1].split('"')[0]
  user_code = find_data.split('name="user_code" value="')[1].split('"')[0]
  encrypted_post_body = find_data.split('name="encrypted_post_body" value="')[1].split('"')[0]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'origin': 'https://mbasic.facebook.com',
                            'upgrade-insecure-requests': '1',
                            'content-type': 'application/x-www-form-urlencoded',
                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                            'referer': url_f,
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'from_post': '1',
                            'deduplicate': '',
                            'link_customer_account': '',
                            'read': '',
                            'link_news_subscription': '',
                            'write': '',
                            'extended': '',
                            'confirm': '',
                            'reauthorize': '',
                            'user_messenger_contact': '',
                            'seen_scopes': '',
                            'response_type': 'code',
                            'auth_type': 'rerequest',
                            'auth_nonce': '',
                            'calling_package_key': '',
                            'default_audience': '',
                            'dialog_type': 'gdp_v4',
                            'fbapp_pres': '',
                            'ret': '',
                            'return_format': 'code',
                            'domain': '',
                            'scope': scope,
                            'sso_device': '',
                            'logger_id': logger_id,
                            'sheet_name': 'initial',
                            'fallback_redirect_uri': '',
                            'sdk': '',
                            'facebook_sdk_version': '',
                            'sdk_version': '',
                            'user_code': user_code,
                            'logged_out_behavior': '',
                            'install_nonce': '',
                            'l_nonce': '',
                            'original_redirect_uri': '',
                            'loyalty_program_id': '',
                            'messenger_page_id': '',
                            'reset_messenger_state': '',
                            'aid': '',
                            'deferred_redirect_uri': '',
                            'code_redirect_uri': '',
                            'extras': '',
                            'tp': 'unspecified',
                            'fx_app': '',
                            'is_promote_auth': '',
                            'encrypted_post_body': encrypted_post_body,
                            'cbt': '',
                            '__CONFIRM__': 'Tiếp+tục'
                        }
  do = requests.post('https://mbasic.facebook.com/v2.0/dialog/oauth/confirm/', headers=headers, data=data)
  url_z = unquote(do.url).split('next=')[1]
  headers = {
                            'Host': 'mbasic.facebook.com',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'save-data': 'on',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'none',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': cookie_fb
                        }
  don = requests.get(url_z, headers=headers).text
  sleep(7)
  driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div/div/div[5]/button[1]/div').click()
  sleep(2)
  ckkk = []
  lis_ck = []
  for x in driver.get_cookies():
      ckkk.append(x['name']+"="+x['value'])
  ck = ';'.join(ckkk)+';'
  lis_ck.append(ck)
  cookierpw = lis_ck[0]
  sleep(5)
  driver.quit()
  return cookierpw
cookierpw = getrpw()
cokiemcn = getmch()
while True:
 for x in range(9):
    try:
       while True:
         x=y+1
         y=x+1
         t33=requests.get("https://rpwliker.com/facebook/posts",headers={
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookierpw
}).text
         t4=t33.split(' <meta name="csrf-token" content="')[1].split('">')[0]
         t3=requests.post("https://rpwliker.com/facebook/autoreaction",headers={
  "x-csrf-token":t4,
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookierpw
},data={
"is_from_local":"0",

"is_from_old_account":"0",

"reaction_type[]":"like",

"post_link":link,

"quantity":"100"
}).text
         check_total = requests.get(f'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={idtds}&hash=AeTkxnH8LFuk5Gk10G0&refid=13', headers = {
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'save-data': 'on',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'none',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cookie': cookie_fb
                        }).text
         total1=check_total.split('role="button" aria-pressed="true" href="')[1].split('">Tất cả ')[0]
         total2=total1.split('total_count=')[1].split(' ')[0]
         sleep(5)
         print("["+str(x)+"]"f"[RPW-LIKER]</>SUCCESS</>{idtds}</>TOTAL:{total2}")
         a=requests.post("https://www.machine-liker.com/api/get-post-info/", headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":cokiemcn},data={"url":url})
         id=a.json()["post"]["id"]
         st=a.json()["post"]["story"]
         url1=f"https://www.machine-liker.com/send-reactions/?post_id={id}&story={st}"
         a=requests.get(url1,headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":cokiemcn})
         obj=a.text.split('name="object_id" value="')[1].split('"')[0]
         bufff=requests.post("https://www.machine-liker.com/api/send-reactions/",headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":cokiemcn},data={"object_id":obj,"reactions":"2","limit":"150"}).text
         like = bufff.json()["info"]["message"].split(" ")[0]
         tonglike = bufff.json()["info"]["total_reactions"]
         if "ok" in bufff:
           print("["+str(y)+"]"f"[MACHINE-LIKER]</>SUCCESS</>{id}</>+{like}REACTION</>TOTAL:{tonglike}")
         else:
           Nghia="Nghia pro "
         sleep(605)
         break
    except:
      sleep(1)
cokiemcn = getmch()
