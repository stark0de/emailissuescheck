import dns.resolver
from colorama import Fore, init
from termcolor import colored
import sys
import os
import subprocess

init()

if len(sys.argv) < 2:
    print(Fore.WHITE+"Usage: python3 emailissuescheck.py listwithdomains verbose")
    sys.exit()

urls=open(sys.argv[1],"r").readlines()
#print(urls)
counter=0
resolver = dns.resolver.Resolver()
for j in urls:
    #print(j.strip)
    try:
       answers = resolver.query(j.strip(), 'TXT')
       #print(answers)
       dkim=0
       print(Fore.GREEN+"[+] Domain with TXT record found "+j.strip()+". Now checking for email security features..."+Fore.WHITE)
       proc = subprocess.Popen("dig +short "+j.strip()+" TXT", shell=True, stdout=subprocess.PIPE)
       i = proc.communicate()[0].decode('utf-8')
       if "DKIM" in i or "dkim" in i:
           print(Fore.RED+"[-] DKIM is enabled in"+j.strip())
           dkim+=1
       if dkim == 0:
           print(Fore.MAGENTA+"[+] DKIM doesn't seem to be enabled")
       print(Fore.WHITE+"Mailspoof analysis:")
       os.system("/home/stark0de/.local/bin/mailspoof -d "+j.strip())
       print("\nIf some SPF misconfiguration is mentioned in the output above please go to: https://emkei.cz/ to send an email PoC so you can demonstrate you are able to spoof the domain source address") 
    except dns.resolver.NoAnswer:
        #print(e,type(e))
        if len(sys.argv) == 3 and sys.argv[2] == "verbose":
           print(Fore.RED+"[-] No TXT record found in"+j.strip())
        continue
    except dns.resolver.NXDOMAIN:
        if len(sys.argv) == 3 and sys.argv[2] == "verbose":
           print(Fore.RED+"[-] Non-existing domain "+j.strip())
        continue
