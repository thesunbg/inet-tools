import requests

def passwordgenerator():
    param = input("Nhập độ dài mật khẩu: ")
    if param == '' :
        return passwordgenerator()
    r = requests.get('https://whois.inet.vn/api/passwordgenerator/'+param+'/strong', json={})
    response = r.json() 
    print(f"""
    Password generator: {response.get('password')}
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
