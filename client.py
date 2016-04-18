#!/usr/bin/python
import requests
import time
import hmac
import hashlib
import json
import argparse

def get(path):
    path_and_query = "/" + path + "?TIMESTAMP=" + str(int(time.time())) + "&ACCOUNT_ID=" + config['id']
    host = config['host']
    sig=hmac.new(str(config['secret']), msg=path_and_query, digestmod=hashlib.sha1).hexdigest()
    return requests.get(host+path_and_query, headers={'X-Auth-Signature': sig})

if __name__ == "__main__":
    with open("client.json") as data_file:
        config = json.load(data_file)

    parser = argparse.ArgumentParser()
    parser.add_argument("endpoint", help="API endpoint to call",
                        type=str)
    args = parser.parse_args()
    
    print get(args.endpoint)
