import requests,os
from time import sleep
print("\033[1;35mCopyright : \033[1;97mPhan Tran Nhan Nghia")
try:
  t = requests.get("https://api.ipify.org/").text
  c = requests.get("https://pastebin.com/raw/wkTZGJhv").text
  t11 = list(reversed(t))
  t22 = ''.join(t11)
  t33 = t22.replace('.', '')
  print(f"\033[1;35mKey Của Bạn Là : \033[1;97m{t33}")
  if t33 in c:
     print("\033[1;92mKey Hoạt Động ")
     sleep(3)
     print("\033[1;92mLoading...")
     sleep(3)
  else:
    print("\033[1;31mVui Lòng Liên Hệ Fb : \033[1;97mNhannghia.phantran.58 \033[1;31mĐể Kích Hoạt Key!! ")
    sleep(0.1)
    exit()
except:
  exit()
os.system("clear")
logo = """\033[1;97m
             ███╗   ██╗██████╗  ██████╗ ███████╗██████╗ 
             ████╗  ██║╚════██╗██╔═████╗╚════██║██╔══██╗
             ██╔██╗ ██║ █████╔╝██║██╔██║    ██╔╝██████╔╝
             ██║╚██╗██║██╔═══╝ ████╔╝██║   ██╔╝ ██╔═══╝ 
             ██║ ╚████║███████╗╚██████╔╝   ██║  ██║     
             ╚═╝  ╚═══╝╚══════╝ ╚═════╝    ╚═╝  ╚═╝ """
print(logo)
print("Coder : Phan Tran Nhan Nghia")
cookiefb=input("Nhập Cookie Facebook: ")
cookie=input("Nhập Cookie Web: ")
link=input("Nhập Link Post: ")
typelike=input("Nhập Type Reactions: ")
def rundelay(k):
  while (k>0):
    
    k=k-1
    print(f'◈ | Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
    print(f'  / Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
    print(f'◈ - Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
    print(f'  \\ Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
tt=requests.post('https://id.traodoisub.com/api.php',data={
  "link":link
})
ttt=tt.json()["id"]
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
headers={
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookie
}
t33=requests.get("https://rpwliker.com/feed",headers=headers).text
t4=t33.split(' <meta name="csrf-token" content="')[1].split('">')[0]
hd={
  "x-csrf-token":t4,
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookie
}
data={
  "send_to": link,
  "quantity": "60",
  "reaction_type[]": typelike,
  "local_only": "0",
  "relevant_accounts_only": "0"
}
stt=0
while True:
  stt=stt+1
  t3=requests.post("https://rpwliker.com/autoreaction",headers=hd,data=data).text
  sleep(65)
  check_dv = requests.get(f'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={ttt}&hash=AeTkxnH8LFuk5Gk10G0&refid=13', headers = {
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
                        'cookie': cookiefb
                        }).text
  t=check_dv.split('role="button" aria-pressed="true" href="')[1].split('">Tất cả ')[0]
  t2=t.split('total_count=')[1].split(' ')[0]
  print(f"[{stt}] SUCCESS </> +100 REACTIONS • TOTAL:{t2}")
  k=550
  rundelay(k)
