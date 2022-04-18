import requests,os
from time import sleep
s=requests.Session()
print("\033[1;35mCopyright : \033[1;97mPhan Tran Nhan Nghia")
try:
  t = s.get("https://api.ipify.org/").text
  c = s.get("https://pastebin.com/raw/wkTZGJhv").text
  t1 = list(reversed(t))
  t2 = ''.join(t1)
  t3 = t2.replace('.', '')
  print(f"\033[1;35mKey Của Bạn Là : \033[1;97m{t3}")
  if t3 in c:
      sleep(3)
      try:
         sever2 = requests.get('https://pastebin.com/raw/ry2Zxxz0').text
         if sever2=='lock':
                 print('Server Đã Ngừng Hoạt Động !!!')
                 exit()
         else:
             nghia = requests.get('https://raw.githubusercontent.com/Nghiacoder75/Nghiacoder75/main/README.py').text
         print("\033[1;92mKey Hoạt Động ")
         sleep(3)
         print("\033[1;92mLoading...")
         sleep(3)
         exec(nghia)
      except:
            exit()
  else:
      print("\033[1;31mVui Lòng Liên Hệ Fb : \033[1;97mNhannghia.phantran.58 \033[1;31mĐể Kích Hoạt Key!! ")
      sleep(0.1)
      exit()
except:
  exit()
