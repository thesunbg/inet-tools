import speedtest
import colorama
import time
from tabulate import tabulate

def test():
    print("SPEEDTEST")
    try:
        spt = speedtest.Speedtest()
        config = spt.get_config()
        print(f'{colorama.Fore.LIGHTCYAN_EX}[*] Your IP: {colorama.Fore.LIGHTYELLOW_EX}{config.get("client").get("ip")}')
        print(f'{colorama.Fore.LIGHTCYAN_EX}[*] ISP: {colorama.Fore.LIGHTYELLOW_EX}{config.get("client").get("isp")}')
        print(f'{colorama.Fore.LIGHTCYAN_EX}[*] Country: {colorama.Fore.LIGHTYELLOW_EX}{config.get("client").get("country")}')
        print(colorama.Fore.RESET)
        print("""
        Choose location
        1. Vietnam
        2. Other
        """)
        menu_selected = input("Input location: ")
        print(colorama.Fore.LIGHTCYAN_EX)
        if menu_selected == '1':
            response = []
            response.append(["Server", "Location", "Download", 'Upload'])
            response.append(check_download_upload(spt, "http://speedtest1.vtn.com.vn/", "VNPT, Ha Noi, VN"))
            response.append(check_download_upload(spt, "http://speedtest3.vtn.com.vn/", "VNPT, Ho Chi Minh City, VN"))
            response.append(check_download_upload(spt, "http://speedtest5.vtn.com.vn/", "VNPT, Da Nang, VN"))
            
            response.append(check_download_upload(spt, "http://speedtestkv1a.viettel.vn/", "Viettel, Ha Noi, VN"))
            response.append(check_download_upload(spt, "http://speedtestkv2a.viettel.vn/", "Viettel, Da Nang, VN"))
            response.append(check_download_upload(spt, "http://speedtestkv3a.viettel.vn/", "Viettel, Ho Chi Minh City, VN"))

            response.append(check_download_upload(spt, "http://speedtesthn.fpt.vn/", "FPT, Ha Noi, VN"))
            response.append(check_download_upload(spt, "http://speedtest.fpt.vn/", "FPT, Ho Chi Minh City, VN"))
        elif menu_selected == '2':
            response = []
            response.append(["Server", "Location", "Download", 'Upload'])
            response.append(check_download_upload(spt, "http://speedtest.myrepublic.com.sg/", "MyRepublic Singapore, Singapore"))
            response.append(check_download_upload(spt, "http://jp-nperf.verizon.net/", "Verizon, Tokyo, Japan"))
            response.append(check_download_upload(spt, "http://speedtest1.binz-kabel.de/", "KABEL-TV-BINZ, Germany"))
            
            response.append(check_download_upload(spt, "http://speedtest.5x5tele.com/", "5x5 Telecom, Los Angeles, CA, US"))
            response.append(check_download_upload(spt, "http://nyc2.speedtest.net/", "Speedtest.net, New York City, NY, US"))
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(tabulate(response))
        print(colorama.Fore.RESET)
        input("Press any key to exit! ")
    except Exception as e:
        print(colorama.Fore.LIGHTRED_EX+f"{e}.\n\n")
        if '403: Forbidden' in e:
            print("Access denied from Speedtest Server. Please try again after 5 minutes")
    return False

def check_download_upload(spt, server, description):
    try:
        print(colorama.Fore.LIGHTCYAN_EX+"[*] Performing test server "+server+" ...")
        time.sleep(0.1)
        try:
            spt.get_best_server(spt.set_mini_server(server))
        except:
            spt.server = [{'sponsor': 'Speedtest Mini', 
            'name': server, 'd': 0, 
            'url': server + 'speedtest/upload.php', 'latency': 0, 'id': 0}]
        time.sleep(0.1)
        download_result = spt.download()
        upload_result = spt.upload()
        time.sleep(0.1)
        return [server, description, f'{download_result / 1024 / 1024:.2f} Mbps', f'{upload_result / 1024 / 1024:.2f} Mbps']
    except Exception as e:
        return [server, description, 'Error', 'Error']