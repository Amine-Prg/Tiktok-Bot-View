#github.com/gamix

import ssl
import requests
from threading import active_count, Thread
from pystyle import Anime, Colorate, Colors, Center , System, Write
from random import randint
from pycenter import center
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
System.Title("𝘎𝘢𝘮𝘪𝘹 - github.com/𝘎𝘢𝘮𝘪𝘹 - 𝘛𝘪𝘬𝘵𝘰𝘬")
class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

x = 0

r = requests.Session()
r.cookies.set_policy(BlockCookies())

def stats(item_id):
    while True:
        try:
            with r.post(f"https://api.toutiao50.com/aweme/v1/aweme/stats/?channel=googleplay&device_type=SM-G9250&device_id={randint(1000000000000000000, 9999999999999999999)}&os_version=10&version_code=220400&app_name=musically_go&device_platform=android&aid=1340", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": "com.zhiliaoapp.musically.go/220400 (Linux; U; Android 10; en_US; SM-G9250; Build/MMB25K.G9250ZTU5DPC5; Cronet/TTNetVersion:5f9540e5 2021-05-20 QuicVersion:47555d5a 2020-10-15)"}, data=f"item_id={item_id}&play_delta=1", stream=True, verify=False) as response:
                if (response.json()["status_code"] == 0):
                    break
                else:
                    continue
        except:
            continue
    
if (__name__ == "__main__"):

    dns_tool = """
   ____                       _        
  / ___|   __ _   _ __ ___   (_) __  __
 | |  _   / _` | | '_ ` _ \  | | \ \/ /
 | |_| | | (_| | | | | | | | | |  >  < 
  \____|  \__,_| |_| |_| |_| |_| /_/\_\


              Tiktok : Gamix_0
                                                    
"""
    print(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter(dns_tool)))

    print(Colorate.Horizontal(Colors.red_to_yellow, "[?] Lien de la vidéo | Gamix  ↓"))
    item_id = str(input(""))
    if ("vm.tiktok.com" in item_id or "vt.tiktok.com" in item_id):
        item_id = r.head(item_id, stream=True, verify=False, allow_redirects=True).url.split("/")[5].split("?", 1)[0]
    else:
        item_id = item_id.split("/")[5].split("?", 1)[0]
    print(Colorate.Horizontal(Colors.red_to_yellow, "[?] Combien de vues voulez vous | Gamix (0 = Infinite) ↓"))
    amount = int(input(""))
    print("")
    print("[i] J'envoie sa de suite | Gamix ...")
    if (amount == 0):
        for _ in iter(int, 1):
            while True:
                if (active_count() <= 5000):
                    print(Colorate.Horizontal(Colors.red_to_yellow, f"Gamix | Vues envoyés: {x}"))
                    x += 1
                    Thread(target=(stats), args=(item_id,)).start()
                    break
    else:
       for _ in range(amount):
            while True:
                if (active_count() <= 5000):
                    print(Colorate.Horizontal(Colors.red_to_yellow, f"Gamix | Vues envoyés: {x}"))
                    x += 1
                    Thread(target=(stats), args=(item_id,)).start()
                    break
