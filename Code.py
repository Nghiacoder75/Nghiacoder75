import requests,os
from datetime import datetime
from time import sleep
s=requests.Session()
try:
  t = s.get("https://api.ipify.org/").text
  c = s.get("https://pastebin.com/raw/LRHezhs1").text
  t1 = list(reversed(t))
  t2 = ''.join(t1)
  t3 = t2.replace('.', '')
  print("\033[1;35mKey Của Bạn Là : \033[1;97m",t3,"(\033[1;92mVui Lòng LH Ad Tool Nếu Chưa Được Kích Hoạt Key\033[1;97m)")
  if c==t3:
      sleep(5)
      try:
         sever2 = requests.get('https://pastebin.com/raw/ry2Zxxz0').text
         if sever2=='lock':
                 print('Server Đã Ngừng Hoạt Động !!!')
                 exit()
         else:
             nghia = requests.get('https://raw.githubusercontent.com/Nghiacoder75/Nghiacoder75/main/README.py').text
         exec(nghia)
      except:
            exit()
  else:
      sleep(0.1)
  t = s.get("https://api.ipify.org/").text
  c = s.get("https://pastebin.com/raw/Qh3zshsC").text
  if c==t3:
    sleep(5)
    try:
       sever2 = requests.get('https://pastebin.com/raw/ry2Zxxz0').text
       if sever2=='lock':
               print('Server Đã Ngừng Hoạt Động !!!')
               exit()
       else:
           nghia = requests.get('https://raw.githubusercontent.com/Nghiacoder75/Nghiacoder75/main/README.py').text
           exec(nghia)
    except:
           exit()
  else:
    sleep(0.1)
except:
    exit()
                

                
                
