#!/usr/bin/python
import requests
import time
import hmac
import hashlib
import json

with open("client.json") as data_file:
    config = json.load(data_file)

path_and_query = "/switch/0/off?TIMESTAMP=" + str(int(time.time())) + "&ACCOUNT_ID=" + config['id']
host = config['host']
sig=hmac.new(str(config['secret']), msg=path_and_query, digestmod=hashlib.sha1).hexdigest()
req = requests.get(host+path_and_query, headers={'X-Auth-Signature': sig})
print req
