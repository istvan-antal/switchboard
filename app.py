#!/usr/bin/python
from flask import Flask
from flask.ext.hmacauth import hmac_auth, DictAccountBroker, HmacManager

from switchboard import SwitchBoard
import json

with open("config.json") as data_file:
    board = SwitchBoard(json.load(data_file)['pins'])

accountmgr = DictAccountBroker(
    accounts={
        "user": {"secret": ";hi^897t7utf", "rights": ["manage"]}
    })

hmacmgr = HmacManager(accountmgr, app)

app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route('/switch/<index>/on')
@hmac_auth("manage")
def turn_on(index):
    board.turn_on(int(index))
    return "on"

@app.route('/switch/<index>/off')
@hmac_auth("manage")
def turn_off(index):
    board.turn_off(int(index))
    return "off"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
