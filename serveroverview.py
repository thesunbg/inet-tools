import psutil
import platform
import time
import colorama
import os

def test():
    print("SYSTEM INFORMATION")
    GB = 1024 * 1024 * 1024
    DAY_SECONDS = 86400
    print(colorama.Fore.LIGHTCYAN_EX +'OS Name: ' +colorama.Fore.LIGHTYELLOW_EX+''+os.name)
    if platform.system() == 'Darwin':
        print(colorama.Fore.LIGHTCYAN_EX +'Platform: '+colorama.Fore.LIGHTYELLOW_EX+'MacOS')
    else:
        print(colorama.Fore.LIGHTCYAN_EX +'Platform: '+colorama.Fore.LIGHTYELLOW_EX+'' +  platform.platform())
    print(colorama.Fore.LIGHTCYAN_EX +'System: ' +colorama.Fore.LIGHTYELLOW_EX+''+platform.system())
    print(colorama.Fore.LIGHTCYAN_EX +'Release: ' +colorama.Fore.LIGHTYELLOW_EX+''+platform.release())
    print(colorama.Fore.LIGHTCYAN_EX +'Uptime: '+colorama.Fore.LIGHTYELLOW_EX+f'{(time.time() - psutil.boot_time())/DAY_SECONDS:.0f} days')

    print(colorama.Fore.LIGHTCYAN_EX +'CPU Model: '+colorama.Fore.LIGHTYELLOW_EX+f'{platform.processor()}')
    print(colorama.Fore.LIGHTCYAN_EX +'CPU Number of Cores: '+colorama.Fore.LIGHTYELLOW_EX+f'{psutil.cpu_count()}')

    memory = psutil.virtual_memory()
    print(colorama.Fore.LIGHTCYAN_EX +'Memory Available: '+colorama.Fore.LIGHTYELLOW_EX+f'{memory.available / (GB):.0f}/{memory.total / (GB):.0f} GB')

    diskUsage = psutil.disk_usage('/')
    print(colorama.Fore.LIGHTCYAN_EX + 'Disk Usage: '+colorama.Fore.LIGHTYELLOW_EX+f'{diskUsage.used / (GB):.0f}/{diskUsage.total / (GB):.0f} GB ({diskUsage.percent}%)')

    if platform.system() != 'Darwin':
        #OSX is not supported.
        procs = [p for p in psutil.process_iter()]
        for p in procs[:]:
            try:
                p._before = p.io_counters()
            except psutil.Error:
                procs.remove(p)
                continue
        disks_before = psutil.disk_io_counters()
        time.sleep(5)
        for p in procs[:]:
            with p.oneshot():
                try:
                    p._after = p.io_counters()
                    p._cmdline = ' '.join(p.cmdline())
                    if not p._cmdline:
                        p._cmdline = p.name()
                    p._username = p.username()
                except (psutil.NoSuchProcess, psutil.ZombieProcess):
                    procs.remove(p)
        disks_after = psutil.disk_io_counters()
        for p in procs:
            p._read_per_sec = p._after.read_bytes - p._before.read_bytes
            p._write_per_sec = p._after.write_bytes - p._before.write_bytes
            p._total = p._read_per_sec + p._write_per_sec

        disks_read_per_sec = disks_after.read_bytes - disks_before.read_bytes
        disks_write_per_sec = disks_after.write_bytes - disks_before.write_bytes
        print(colorama.Fore.LIGHTCYAN_EX + 'Disk read: ' + colorama.Fore.LIGHTYELLOW_EX+f'{disks_read_per_sec}')
        print(colorama.Fore.LIGHTCYAN_EX + 'Disk write: ' + colorama.Fore.LIGHTYELLOW_EX+f'{disks_write_per_sec}')
    print(colorama.Fore.RESET)
    input("Press any key to exit! ")
    return False