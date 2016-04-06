#!/usr/bin/python
import requests
import time
import hmac
import hashlib

path_and_query = "/switch/0/off?TIMESTAMP="+str(int(time.time())) + "&ACCOUNT_ID=user"
host = "http://192.168.0.121:5000"
sig=hmac.new("please randomly generate me", msg=path_and_query, digestmod=hashlib.sha1).hexdigest()
req = requests.get(host+path_and_query, headers={'X-Auth-Signature': sig})
print req
