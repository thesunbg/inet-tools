import speedtest
import colorama
import time

def test():
    print("SPEED TEST ")
    try:
        spt = speedtest.Speedtest()
        print(colorama.Fore.LIGHTCYAN_EX+"[*] Checking best server...")
        get = spt.get_best_server()
        # print(get)
        check_download_upload(spt, "http://speedtest1.vtn.com.vn/", "VNPT, Ha Noi, VN")
        check_download_upload(spt, "http://speedtest3.vtn.com.vn/", "VNPT, Ho Chi Minh City, VN")
        check_download_upload(spt, "http://speedtest5.vtn.com.vn/", "VNPT, Da Nang, VN")
        
        check_download_upload(spt, "http://speedtestkv1a.viettel.vn/", "Viettel, Ha Noi, VN")
        check_download_upload(spt, "http://speedtestkv2a.viettel.vn/", "Viettel, Da Nang, VN")
        check_download_upload(spt, "http://speedtestkv3a.viettel.vn/", "Viettel, Ho Chi Minh City, VN")

        check_download_upload(spt, "http://speedtesthn.fpt.vn/", "FPT, Ha Noi, VN")
        check_download_upload(spt, "http://speedtest.fpt.vn/", "Ho Chi Minh City, Ho Chi Minh City, VN")
         
    except Exception:
        print(colorama.Fore.LIGHTRED_EX+"Error: Check your Internet Connection.\n\n")
    return False

def check_download_upload(spt, server, description):
    try:
        print(colorama.Fore.LIGHTCYAN_EX+"[*] Performing test server "+server+" ...")
        time.sleep(0.1)
        spt.set_mini_server(server)
        time.sleep(0.1)
        download_result = spt.download()
        upload_result = spt.upload()
        time.sleep(0.1)
        print(colorama.Fore.LIGHTCYAN_EX+"[+] Server: " + server + " (" + description + ")")
        print(colorama.Fore.LIGHTCYAN_EX+"Download speed:"+colorama.Fore.LIGHTYELLOW_EX+f" {download_result / 1024 / 1024:.2f} Mbps")
        print(colorama.Fore.LIGHTCYAN_EX+"Upload speed:"+colorama.Fore.LIGHTYELLOW_EX+f" {upload_result / 1024 / 1024:.2f} Mbps")
        print(colorama.Fore.RESET)
    except Exception as e:
        print(colorama.Fore.LIGHTRED_EX+"Server: " + server + " error!")
        print(colorama.Fore.RESET)
