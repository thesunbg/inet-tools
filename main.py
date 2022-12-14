import pyfiglet

import serveroverview
import speedtesttools
import whois
import checkhost

def menu():
    print(pyfiglet.figlet_format("iNET Tools"))
    print("""
    0. Exit
    1. Server Information (OS, CPU, Memory, Disk ...)
    2. Speedtest (Use Speedtest.net)
    3. Whois (All tlds: .com, .vn, .net, .xyz, ...)
    4. Check host (PING, HTTP, TCP)
    """)
    menu_selected = input("Select tools: ")
    if menu_selected == '0':
        print("Bye!")
        return False
    elif menu_selected == '1':
        while(serveroverview.test()):
            pass
    elif menu_selected == '2':
        while(speedtesttools.test()):
            pass
    elif menu_selected == '3':
        while(whois.test()):
            pass
    elif menu_selected == '4':
        while(checkhost.test()):
            pass
    return True

while(menu()):
   pass
