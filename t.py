import requests
import json
import time
import sys
import os
import platform
# /** api Web by nakocoders **/
os.system("clear")
print "[\033[91m!\033[00m] \033[93mPaypal Checker Valid \033[00m[\033[91m!\033[00m]"
print "\033[96mIni Manual Ea Bgsd\033[00m"
print "Klo Mau Yg Otomatis Tungguin Ajg Gua Puyeng >:( \n"

gegek = raw_input("masukan domain host : ")
req = requests.get("https://nakocoders.org/paypal/api.php?e='+gegek")
st = json.loads(req.content)
status = (st["status"])
print "\033[96m|_______\033[92mEmail\033[96m__\033[96m_________\033[92mstatus\033[96m___|"
print "|\033[93m %s \033[91m|\033[95m  %s \033[91m|\033[00m"% (gegek,status) 
