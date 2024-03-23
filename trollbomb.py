# -*- coding: UTF-8 -*- 

import pyautogui as pg 
import colorama
import time 
from colorama import Fore,Back,Style

isim = r'''

  __                .__  .__ ___.                 ___.    
_/  |________  ____ |  | |  |\_ |__   ____   _____\_ |__  
\   __\_  __ \/  _ \|  | |  | | __ \ /  _ \ /     \| __ \ 
 |  |  |  | \(  <_> )  |_|  |_| \_\ (  <_> )  Y Y  \ \_\ \
 |__|  |__|   \____/|____/____/___  /\____/|__|_|  /___  /
                                  \/             \/    \/ '''

print(Fore.LIGHTBLUE_EX+isim)
print(Fore.LIGHTBLACK_EX+"                                               BY : NYOXS\n                                               v 1.0\n")


mesaj=input(Fore.RED+"[+] GÖNDERİLECEK MESAJ: ")
mesajsayısı=int(input(Fore.RED+"\n\n\n[+] MESAJ ADEDİ: "))



if mesajsayısı==1:
    print("")
else:
    saniye=int(input(Fore.RED+"\n\n\n[+] KAÇ SANİYE ARALIKLA GÖNDERMEK İSTERSİNİZ: "))


saniye2=int(input(Fore.RED+"\n\n\n[+] KAÇ SANİYE SONRA BAŞLAMASINI İSTERSİNİZ: "))
time.sleep(3)
print(Fore.GREEN+"\n\n\n[✓] HAZIRLANDI")

time.sleep(saniye2)

for döngü in range(mesajsayısı):

    if mesajsayısı==1:
        time.sleep(0.1)
        pg.write(mesaj)
        pg.press("Enter")
    else:
       time.sleep(saniye)
       pg.write(mesaj)
       pg.press("Enter")


    
print(Fore.LIGHTBLACK_EX+"\n\n\n[*] BİZİ TERÇİH ETTİGİNİZ İÇİN TEŞEKKÜRLER :)")
     
   