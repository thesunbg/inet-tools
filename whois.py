import requests
import colorama

def test():
    print("WHOIS")
    param = input("Input a domain: ")
    if param == '' :
        return test()
    print("Loading ... ")
    r = requests.get('https://whois.inet.vn/api/whois/domainspecify/' + param, json={})
    response = r.json() 

    print(colorama.Fore.LIGHTCYAN_EX + 'Message: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("message")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Code: ' + colorama.Fore.LIGHTYELLOW_EX+f'{"Not register" if response.get("code") == "1" else "Registered"}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Domain Name: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("domainName")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Registrar: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("registrar")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Registrant: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("Registrant")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Creation Date: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("creationDate")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Expiry Date: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("expirationDate")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Name Server: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("nameServer")}')
    print(colorama.Fore.LIGHTCYAN_EX + 'Status: ' + colorama.Fore.LIGHTYELLOW_EX+f'{response.get("status")}')
    print(colorama.Fore.RESET)
    return False
