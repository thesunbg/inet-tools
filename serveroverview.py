import psutil
import platform
from time import time
import colorama
import os
import sys
from random import shuffle

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
    print(colorama.Fore.LIGHTCYAN_EX +'Uptime: '+colorama.Fore.LIGHTYELLOW_EX+f'{(time() - psutil.boot_time())/DAY_SECONDS:.0f} days')

    print(colorama.Fore.LIGHTCYAN_EX +'CPU Model: '+colorama.Fore.LIGHTYELLOW_EX+f'{platform.processor()}')
    print(colorama.Fore.LIGHTCYAN_EX +'CPU Number of Cores: '+colorama.Fore.LIGHTYELLOW_EX+f'{psutil.cpu_count()}')

    memory = psutil.virtual_memory()
    print(colorama.Fore.LIGHTCYAN_EX +'Memory Available: '+colorama.Fore.LIGHTYELLOW_EX+f'{memory.available / (GB):.0f}/{memory.total / (GB):.0f} GB')

    diskUsage = psutil.disk_usage('/')
    print(colorama.Fore.LIGHTCYAN_EX + 'Disk Usage: '+colorama.Fore.LIGHTYELLOW_EX+f'{diskUsage.used / (GB):.0f}/{diskUsage.total / (GB):.0f} GB ({diskUsage.percent}%)')
    
    disk_tesk = DiskTest('/tmp/disktest', 128, 1024, 512)
    disk_tesk.print()
    print(colorama.Fore.RESET)
    input("Press any key to exit! ")
    return False

class DiskTest:
    def __init__(self, file,write_mb, write_block_kb, read_block_kb):
        self.file = file
        self.write_mb = write_mb
        self.write_block_kb = write_block_kb
        self.read_block_kb = read_block_kb
        wr_blocks = int(self.write_mb * 1024 / self.write_block_kb)
        rd_blocks = int(self.write_mb * 1024 * 1024 / self.read_block_kb)
        self.write_results = self.write_test( 1024 * self.write_block_kb, wr_blocks)
        self.read_results = self.read_test(self.read_block_kb, rd_blocks)

    def write_test(self, block_size, blocks_count, show_progress=True):
        f = os.open(self.file, os.O_CREAT | os.O_WRONLY, 0o777)  # low-level I/O

        took = []
        for i in range(blocks_count):
            if show_progress:
                sys.stdout.write('\rWriting percent: {:.2f} %'.format(
                    (i + 1) * 100 / blocks_count))
                sys.stdout.flush()
            buff = os.urandom(block_size)
            start = time()
            os.write(f, buff)
            os.fsync(f)
            t = time() - start
            took.append(t)

        os.close(f)
        return took

    def read_test(self, block_size, blocks_count, show_progress=True):
        f = os.open(self.file, os.O_RDONLY, 0o777)
        offsets = list(range(0, blocks_count * block_size, block_size))
        shuffle(offsets)

        took = []
        for i, offset in enumerate(offsets, 1):
            if show_progress and i % int(self.write_block_kb * 1024 / self.read_block_kb) == 0:
                sys.stdout.write('\rReading percent: {:.2f} %'.format(
                    (i + 1) * 100 / blocks_count))
                sys.stdout.flush()
            start = time()
            os.lseek(f, offset, os.SEEK_SET) 
            buff = os.read(f, block_size)
            t = time() - start
            if not buff: break
            took.append(t)

        os.close(f)
        return took

    def print(self):
        result = ('\n\nWritten {} MB in {:.4f} s\nWrite speed is  {:.2f} MB/s'
                    '\n  max: {max:.2f}, min: {min:.2f}\n'.format(
            self.write_mb, sum(self.write_results), self.write_mb / sum(self.write_results),
            max=self.write_block_kb / (1024 * min(self.write_results)),
            min=self.write_block_kb / (1024 * max(self.write_results))))
        result += ('\nRead {} x {} B blocks in {:.4f} s\nRead speed is  {:.2f} MB/s'
                    '\n  max: {max:.2f}, min: {min:.2f}\n'.format(
            len(self.read_results), self.read_block_kb,
            sum(self.read_results), self.write_mb / sum(self.read_results),
            max=self.read_block_kb / (1024 * 1024 * min(self.read_results)),
            min=self.read_block_kb / (1024 * 1024 * max(self.read_results))))
        print(result)        
