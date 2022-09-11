import pyfiglet

import serveroverview
import speedtesttools
import whois
import checkhost

def menu():
    print(pyfiglet.figlet_format("iNET Tools"))
    print("""
    0. Exit
    1. Server Information (OS, CPU, Memory, Disk...)
    2. Speedtest (Using Speedtest.net)
    3. Whois (All tld: .com, .vn, .net, .xyz, ...)
    4. Check host (Ping, HTTP, TCP)
    """)
    menu_selected = '-1'
    try:
        menu_selected = input("Input tools: ")
    except EOFError:
        pass
    if menu_selected == '0':
        print("Goodbye!")
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
