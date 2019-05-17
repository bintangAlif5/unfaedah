
import os, sys, time, json, requests

green = '\033[32;1m'
white = '\033[0m'
blue = '\033[36;1m'
yellow = '\033[33;1m'
red = '\033[31;1m'
purple = '\033[35;1m'

os.system("clear")
time.sleep(2)
os.system('figlet Yahoo Checker')
star = """
\033[93m##################################### 
# \033[91mAuthor : \033[96mr00t@star.\033[93m                            
# \033[91mTeam : \033[96mSunda Cyber Army\033[93m 
# \033[91mDate : \033[96m17 - 05 - 2019\033[93m        
# \033[91mfacebook : \033[96mhttps://www.facebook.com/BintangAlifff\033[93m 
# \033[91mInstaGram : \033[96m@bintang_alif16\033[93m
# \033[91mNote : \033[96mJika error silahkan hubungi saya, jika ingin Auto Bikin wordlist baru\033[93m
#############################################
"""
print ""
print star 
print "\033[93mMau Auto apa kgaa?\n 1). Ya\n 2). Tidak"
putput = raw_input("input --> \033[95m")
if putput == "1":
   gudd = raw_input("Masukan Nama Wordlistnya : ")
   aerr = open("'+gudd'", "r")
   ct = aerr.read().splitlines() 
   r = requests.get("http://widhitools.000webhostapp.com/api/yahoo.php?email="+ct)
   print green+"[!] "+blue+"Account : "+red, r.json()["email"]
   print green+"[!] "+blue+"Status  : "+red, r.json()["status"]
   
if putput == "2":
   print "\033[91mOkei Manual zuahaha"
   mal = raw_input("Masukan Emailna: ")
   r = requests.get("http://widhitools.000webhostapp.com/api/yahoo.php?email="+mal)
   print green+"[!] "+blue+"Account : "+red, r.json()["email"]
   print green+"[!] "+blue+"Status  : "+red, r.json()["status"]
   
