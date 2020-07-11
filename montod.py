import os
import sys
import time
os.system('clear')
os.system('figlet SCH-T')
print "======================="
print "Author : SCH-T"
print "YouTube : Shinchan Tutorial"
print "Country : Indonesia"
print "======================="
print
time.sleep(1)
print "[+] Menu Pilihan [+]"
print "[1] Moonton Checker dz-id"
print "[2] SCH-T Checker"
print "[3] Ping server"
time.sleep(1)
pilih = raw_input('[?] pilih : ')
if pilih == "1":
          os.system('git clone https://github.com/dz-id/MoontonChecker')
          print "[+] Penginstalan selesai"
          time.sleep(1)
          print "[+] Selanjutnya ketik $ cd MoontonChecker"
          time.sleep(1)
          print "[+] Lalu ketik $ python moonton.py"
elif pilih == "2":
          os.system('pkg update')
          os.system('pkg install bash')
          os.system('git clone https://github.com/SuProjec/SCH-T')
          time.sleep(1)
          print "[+] penginstalan selesai"
          time.sleep(1)
          print "[+] selanjutnya $ cd SCH-T"
          time.sleep(1)
          print "[+] Lalu ketik bash scht.sh"
elif pilih == "3":
          os.system('ping 8.8.8.8')