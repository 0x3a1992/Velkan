from rich import print

import requests 
from datetime import datetime


def finder(args):

    if args.url == None:
        print(f"[red] [!] Error witre url [white]")   
    elif args.wordlist == None:
        print(f"[red] [!] Error witre path wordlist [white]")
    else:
        date_now = datetime.now().strftime("%m-%d-%Y - %H-%M-%S")

        print(f"[purple] [+] [white]Url: {args.url}")
        print(f"[purple] [+] [white]Wordlist: {args.wordlist}\n")

        file = open(args.wordlist, 'r')
        
        for word in file:
            
            read = word.rstrip('\n')
            
            subdomain = 'http://' + read + '.' + args.url

            try:
                request = requests.get(subdomain)             
                print(f"[green] [200] [OK] [white] {subdomain} ")
            except Exception:
                print(f"[red] [ERROR] [white] {subdomain}")

                

                
            


    


