import requests

def test():
    print("WHOIS")
    param = input("Input a domain: ")
    if param == '' :
        return test()
    print("Loading ... ")
    r = requests.get('https://whois.inet.vn/api/whois/domainspecify/' + param, json={})
    response = r.json() 
    print(f"""
    Done
    Message: {response.get('messsage')}
    Code: {"Not register" if response.get('code') == '1' else "Registered"}
    Domain Name: {response.get('domainName')}
    Registrar: {response.get('registrar')}
    Registrant: {response.get('registrant')}
    Creation Date: {response.get('creationDate')}
    Expiry Date: {response.get('expirationDate')}
    """)

    step = input(f"""
    Continue?:
    y - yes
    n - no
    """)
    if step == 'y':
        return True
    else:
        return False
