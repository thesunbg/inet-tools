import requests
import time
from tabulate import tabulate
import colorama

def test():
    print("CHECK HOST")
    print("""
        Choose type
        1. ping
        2. http
        3. tcp
        """)
    menu_selected = input("Input type: ")
    type = 'ping'
    if menu_selected == '2':
        type = 'http'
    elif menu_selected == '3':
        type = 'tcp'
    param = input("Input a host (domain:port, default port 80): ")
    if param == '' :
        return test()
    print("Testing "+type+" host: "+param+" ... ")
    r = requests.get('https://check-host.net/check-'+type+'?max_nodes=25&host=' + param, 
    headers={"Accept":"application/json"},
    json={})
    response = r.json()
    time.sleep(10)
    if response.get("request_id") is not None:
        r = requests.get('https://check-host.net/check-result/' + response.get("request_id"), 
        headers={"Accept":"application/json"},
        json={})
        response = r.json()
        print(response)
        if type == 'http':
            result = []
            result.append(["Location", "Result", "Time (s)", "Text", "Response Code", "IP address"])
            for key in response:
                value = response[key]
                result.append([mapping_host(key), 'OK' if value[0][0] == 1 else f'{colorama.Fore.LIGHTRED_EX}ERROR{colorama.Fore.LIGHTYELLOW_EX}', 
                value[0][1], value[0][2], value[0][3], value[0][4]])
        elif type == 'ping':
            result = []
            result.append(["Location", "Result", "Time (s)", "IP address"])
            for key in response:
                value = response[key]
                result.append([mapping_host(key), 'OK' if value[0][0][0] == 'OK' else f'{colorama.Fore.LIGHTRED_EX}ERROR{colorama.Fore.LIGHTYELLOW_EX}', 
                value[0][0][1], value[0][0][2]])
        elif type == 'tcp':
            result = []
            result.append(["Location", "Result", "Time (s)", "IP address"])
            for key in response:
                value = response[key]
                if not value[0].get('error') is None:
                    pingResult = f'{colorama.Fore.LIGHTRED_EX}ERROR{colorama.Fore.LIGHTYELLOW_EX}'
                    pingTime = 0
                    pingAddress = ''
                else:
                    pingResult = 'OK'
                    pingTime = value[0].get('time')
                    pingAddress = value[0].get('address')
                result.append([mapping_host(key), pingResult, 
                pingTime, pingAddress])
        elif type == 'dns':
            result = []
            result.append(["Location", "Result", "Time (s)", "IP address"])
            for key in response:
                value = response[key]
                result.append([mapping_host(key), 'OK' if value[0][0][0] == 'OK' else f'{colorama.Fore.LIGHTRED_EX}ERROR{colorama.Fore.LIGHTYELLOW_EX}', 
                value[0][0][1], value[0][0][2]])
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(tabulate(result))
        print(colorama.Fore.RESET)
    return False

def mapping_host(hostname):
    if hostname == 'at1.node.check-host.net':
        return 'Austria, Vienna'
    elif hostname == 'cz1.node.check-host.net':
        return 'Czechia, C.Budejovice'
    elif hostname == 'fi1.node.check-host.net':
        return 'Finland, Helsinki'
    elif hostname == 'de4.node.check-host.net':
        return 'Germany, Frankfurt'
    elif hostname == 'hk1.node.check-host.net':
        return 'Hong Kong, Hong Kong'
    elif hostname == 'ir1.node.check-host.net':
        return 'Iran, Tehran'
    elif hostname == 'it2.node.check-host.net':
        return 'Italy, Milan'
    elif hostname == 'kz1.node.check-host.net':
        return 'Kazakhstan, Karaganda'
    elif hostname == 'lt1.node.check-host.net':
        return 'Lithuania, Vilnius'
    elif hostname == 'md1.node.check-host.net':
        return 'Moldova, Chisinau'
    elif hostname == 'nl1.node.check-host.net':
        return 'Netherlands, Amsterdam'
    elif hostname == 'pl1.node.check-host.net':
        return 'Poland, Olsztyn'
    elif hostname == 'pt1.node.check-host.net':
        return 'Portugal, Viana'
    elif hostname == 'ru4.node.check-host.net':
        return 'Russia, Ekaterinburg'
    elif hostname == 'ru1.node.check-host.net':
        return 'Russia, Moscow'
    elif hostname == 'ru2.node.check-host.net':
        return 'Russia, Moscow'
    elif hostname == 'ru3.node.check-host.net':
        return 'Russia, Novosibirsk'
    elif hostname == 'rs1.node.check-host.net':
        return 'Serbia, Belgrade'
    elif hostname == 'ch1.node.check-host.net':
        return 'Switzerland, Zurich'
    elif hostname == 'tr1.node.check-host.net':
        return 'Turkey, Istanbul'
    elif hostname == 'ua1.node.check-host.net':
        return 'Ukraine, Khmelnytskyi'
    elif hostname == 'ua2.node.check-host.net':
        return 'Ukraine, Kyiv'
    elif hostname == 'us3.node.check-host.net':
        return 'USA, Atlanta'
    elif hostname == 'us1.node.check-host.net':
        return 'USA, Los Angeles'
    else:
        return hostname