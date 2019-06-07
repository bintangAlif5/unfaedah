#python bukan python2

from urllib.request import urlopen, Request, URLError, HTTPError
import sys
import time, random
def Y(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)

print('''\033[93m
     _       _           _         _             _       
    / \   __| |_ __ ___ (_)_ __   | | ___   __ _(_)_ __  
   / _ \ / _` | '_ ` _ \| | '_ \  | |/ _ \ / _` | | '_ \ 
  / ___ \ (_| | | | | | | | | | | | | (_) | (_| | | | | |
 /_/   \_\__,_|_| |_| |_|_|_| |_| |_|\___/ \__, |_|_| |_|
                                           |___/         
''')
def p3ng(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(10./100)
Y("\033[95mEasy coding python awoakawoak:v")
Y("\033[93mAuthor : Star Gans")
Y("\033[92mSpesial thx : Sunda Cyber Army")
Y("\033[98mdefault Wordlist: word.txt")
Y("\033[91mAnda Bisa Membuat wordlist Baru h3h3")
print ("___________________________________________")
sw = input("Nama wordlist lu gayn :\033[96m ")
header = {'user-agent': 'Mozilla/5.0 (Windows NT 5.0; rv:14.0) Gecko/20100101 Firefox/14.0.1'}
file = open(sw, 'r').read().split('\n')
site = input('\033[95mMasukan Link: ')
p3ng("\033[94mMencari Admin Login...\033[0m")
for list in file:
    url = site + '/' +list
    try:
        req = Request(url, None, header)
        res = urlopen(req)
    except(ValueError, HTTPError, URLError):
        print('\033[31;1mTidak Ditemukan: ' + url + '\033[0m')
    else:
        print('\033[32;1mBerhasil Ditemukan: ' + url + '\033[0m')
