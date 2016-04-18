#!/usr/bin/python
import requests
import time
import hmac
import hashlib
import json
import argparse

class Client(object):
    def __init__(self, config):
        self._config = config
        if "id" not in config:
            self._config["id"] = "user"

    def get(self, path):
        path_and_query = "/" + path + "?TIMESTAMP=" + str(int(time.time())) + "&ACCOUNT_ID=" + self._config['id']
        host = self._config['host']
        sig=hmac.new(str(self._config['secret']), msg=path_and_query, digestmod=hashlib.sha1).hexdigest()
        return requests.get(host+path_and_query, headers={'X-Auth-Signature': sig})

if __name__ == "__main__":
    with open("client.json") as data_file:
        client = Client(json.load(data_file))

    parser = argparse.ArgumentParser()
    parser.add_argument("endpoint", help="API endpoint to call",
                        type=str)
    args = parser.parse_args()

    print client.get(args.endpoint)