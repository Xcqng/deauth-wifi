import time 
import sys,os

os.system("airmon-ng")
time.sleep(3)
os.system("clear")
os.system("airmon-ng start wlan0")
os.system("clear")
os.system("figlet -f mono9  DeAutH ?  WIFI | lolcat  ")
time.sleep(3)
os.system("airodump-ng wlan0mon")
bssid = raw_input("ENTER BSSID : ")
channel = raw_input("ENTER NUMBER CHANNEL : ")
os.system("airodump-ng wlan0mon --bssid %s --channel %s"%(bssid, channel))
os.system("python aireplay.py")
