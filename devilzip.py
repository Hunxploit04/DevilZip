import zipfile
import time
from sys import stderr
import os

#\033[34;1m
#\033[32;1m
#\033[35;1m
#\033[36;1m
#\033[31;1m
#\033[37;1m
#\033[33;1m

def banner():
     stderr.writelines("""\033[34;1m                                                      
,------.                  ,--.,--.,-------.,--.        
|  .-.  \  ,---.,--.  ,--.`--'|  |`--.   / `--' ,---.  
|  |  \  :| .-. :\  `'  / ,--.|  |  /   /  ,--.| .-. | 
|  '--'  /\   --. \    /  |  ||  | /   `--.|  || '-' ' 
`-------'  `----'  `--'   `--'`--'`-------'`--'|  |-'  
                                               `--'    
      \033[34;1m..:: \033[33;1mTools Cracking Zip By HunX \033[34;1m::..
""")
banner()

fileZip = input("\n\033[37;1mEnter File Zip : \033[34;1m")
print()

wordlist = "password.txt"

with zipfile.ZipFile(fileZip) as zf:
    with open(wordlist, "r") as wr:
        for line in wr:
            password = line.strip()
            try:
                zf.extractall(pwd=password.encode())
                print()
                print("\033[31;1m===========================")
                print(f"\033[37;1m| Password ditemukan: \033[34;1m{password}\033[37;1m |")
                print("\033[31;1m===========================")
                break
            except:
                print(f"\033[37;1m[\033[33;1m-\033[37;1m] \033[37;1mPassword salah: \033[31;1m{password}")
