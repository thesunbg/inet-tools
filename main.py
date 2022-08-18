import pyfiglet

import serveroverview
import speedtesttools
import whois


def menu():
    print(pyfiglet.figlet_format("Python Tools"))
    print("""
    0. Exit
    1. Server Information (OS, CPU, Memory, Disk, IP public...)
    2. Speedtest
    3. Whois
    """)
    menu_selected = input("Input tools: ")
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
    return True

while(menu()):
   pass
