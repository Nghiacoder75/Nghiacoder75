
from time import sleep
import base64
import warnings,threading
from six.moves.urllib_parse import urljoin
import os,json,requests,string, base64, six
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import unquote
from anycaptcha import *


 

os.system('clear')
os.system('cls')
def logo():
    logo = """\033[1;35m
             ███╗   ██╗██████╗  ██████╗ ███████╗██████╗ 
             ████╗  ██║╚════██╗██╔═████╗╚════██║██╔══██╗
             ██╔██╗ ██║ █████╔╝██║██╔██║    ██╔╝██████╔╝
             ██║╚██╗██║██╔═══╝ ████╔╝██║   ██╔╝ ██╔═══╝ 
             ██║ ╚████║███████╗╚██████╔╝   ██║  ██║     
             ╚═╝  ╚═══╝╚══════╝ ╚═════╝    ╚═╝  ╚═╝ """
    print(logo)
    print('\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=')
    print('\033[1;96m CODER: \033[1;97mNHÂN NGHĨA                  \033[1;96mYOUTUBE: \033[1;97mNHÂN NGHĨA OFFICIAL  \n\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=');
    print(' \033[1;96mMOMO: \033[1;97m0852440015                \033[1;96mTOOL: \033[1;97mMACHINE LIKER BYPASS CAPTCHA')
    print('\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=\033[1;35m=\033[1;97m=')
    print('       \033[1;96m© 2021 - Thiết Kế Và Vận Hành Bởi Phan Trần Nhân Nghĩa')
    print('\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=\033[1;33m=\033[1;91m=')
logo()
apikey ="94b30656482647fc990788b93b16a99d"
#apikey= str(input("~ \033[1;33m[\033[1;35m✓\033[1;33m] \033[1;97mNhập \033[1;97mApi Key Anycaptcha: \033[1;35m"))
data = {"clientKey":apikey }
try:
            bal = requests.post('https://api.anycaptcha.com/getBalance',data=data).json()["balance"]
            print(f"~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mSố Balance Trong Anycaptcha : \033[1;35m{bal} $")
except:
            print("\033[1;37mApi Key Anycaptcha Sai !!")
            exit()
user = input("~ \033[1;33m[\033[1;35m✓\033[1;33m] \033[1;97mNhập User-Agent: \033[1;35m")
soluong = int(input("~ \033[1;33m[\033[1;35m✓\033[1;33m] \033[1;97mNhập Số Luồng: \033[1;35m"))
data_cookie_fb = []
data_urlbaiviet = []
data_type = []
for i in range(soluong):
    cookie_fbb = str(input(f"~ \033[1;33m[\033[1;35m✓\033[1;33m] \033[1;97mNhập Cookie Facebook Thứ {i}: \033[1;35m"))
    headers = {
            'cookie': cookie_fbb
        }
        
    try:
            find_data = requests.get("https://m.facebook.com/", headers=headers).text
            aaaaaa = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
            data_cookie_fb.append(cookie_fbb)

    except:
            print("COOKIE DIE!!!")
            continue
    urlbaiviett = str(input(f'~ \033[1;33m[\033[1;35m✓\033[1;33m] \033[1;97mLink Bài Viết Thứ {i}: \033[1;35m'))
    data_urlbaiviet.append(urlbaiviett)
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m1\033[1;97m] \033[1;97mLIKE ")
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m2\033[1;97m] \033[1;97mLOVE")
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m3\033[1;97m] \033[1;97mWOW")
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m4\033[1;97m] \033[1;97mHAHA")
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m7\033[1;97m] \033[1;97mSAD")
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m8\033[1;97m] \033[1;97mANGRY")
    print("~ \033[1;33m[\033[1;97m+\033[1;33m] \033[1;97mCHỌN \033[1;97m[\033[1;91m16\033[1;97m] \033[1;97mCre")
    print("- "*31)
    typee=input("~ \033[1;33m[\033[1;35m✓\033[1;33m] \033[1;97mNhập Cảm Xúc Muốn Buff VD:(1,2,3,16,..) : \033[1;35m")
    data_type.append(typee)
stt=0
def chay(i):
    global stt
    url = data_urlbaiviet[i]
    cookie_fb = data_cookie_fb[i]
    type = data_type[i]
    while True:
        headersaa = {
            'cookie': cookie_fb
        }
        
        try:
                find_dataa = requests.get("https://m.facebook.com/", headers=headersaa).text
                aaaaaa = find_dataa.split('name="fb_dtsg" value="')[1].split('"')[0]
        except:
                print("COOKIE DIE!!!")
                break
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
        while True:
            try:
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
                try:
                            fb_dtsg = check_dv.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
                            jazoest = check_dv.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
                            qr = check_dv.split('name="qr" value="')[1].split('"')[0]
                except:
                            print('Cookie die')
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
                don = requests.get(url_z, headers=headers)
                break
            except:
                continue
        
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
        while True:
                a=requests.post("https://www.machine-liker.com/api/get-post-info/", headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":ck},data={"url":url})
                try:
                    id=a.json()["post"]["id"]
                    st=a.json()["post"]["story"]
                except:
                    break
                url1=f"https://www.machine-liker.com/send-reactions/?post_id={id}&story={st}"
                a=requests.get(url1,headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":ck})
                obj=a.text.split('name="object_id" value="')[1].split('"')[0]
                d=0
                
                bufff=requests.post("https://www.machine-liker.com/api/send-reactions/",headers={"Host":"www.machine-liker.com","x-requested-with":"XMLHttpRequest","user-agent":user,"origin":"https://www.machine-liker.com","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"https://www.machine-liker.com/auto-reactions/","cookie":ck},data={"object_id":obj,"reactions":type,"limit":"150"})
                if "info" in bufff.text:
                    cong=bufff.json()["info"]["message"].split(" ")[0]
                    tong=bufff.json()["info"]["total_reactions"]
                    from datetime import datetime
                    t=datetime.now().strftime('%H:%M:%S')
                    stt = stt+1
                    print(f"\033[0;95m[\033[1;93m{stt}\033[0;95m]\033[1;97m Nhan \033[1;97mNghia \033[1;96m● \033[1;93m{t} \033[1;96m● \033[1;97m{id} \033[1;96m● \033[1;97m\033[1;93m{cong} \033[1;92mReactions \033[1;96m● \033[1;97mTổng: \033[1;93m{tong} \033[1;92mReactions")
                else:
                    from datetime import datetime
                    t=datetime.now().strftime('%H:%M:%S')
                for ti in range(610 , 0, -1):
                    print(f'\033[1;97m◈ \033[1;35m[\033[1;93m|\033[1;31m] \033[0;36mVui Lòng Đợi {ti} Giây  ',end='\r')
                    sleep(0.200)
                    print(f'  \033[1;31m[\033[1;92m/\033[1;35m] \033[0;36mVui Lòng Đợi {ti} Giây  ',end='\r')
                    sleep(0.200)
                    print(f'\033[1;96m◈ \033[1;35m[\033[0;36m-\033[1;31m] \033[0;36mVui Lòng Đợi {ti} Giây  ',end='\r')
                    sleep(0.200)
                    print(f'  \033[1;31m[\033[1;35m\\\033[1;35m] \033[0;36mVui Lòng Đợi {ti} Giây  ',end='\r')
                    sleep(0.200)
                    print(f'\033[1;96m◈ \033[1;35m[\033[0;36m-\033[1;31m] \033[0;36mVui Lòng Đợi {ti} Giây  ',end='\r')
                    sleep(0.200) 

    
for i in range(soluong):
		khoitao = threading.Thread(target=chay,args=(i,)).start()
