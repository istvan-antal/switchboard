#!/usr/bin/python
from flask import Flask
from flask.ext.hmacauth import hmac_auth, DictAccountBroker, HmacManager

from switchboard import SwitchBoard
import json
from desklamp import DeskLamp

with open("config.json") as data_file:
    config = json.load(data_file)

board = SwitchBoard(config['pins'])
desklamp = DeskLamp(board=board, pinIndex=0)
app = Flask(__name__)

accountmgr = DictAccountBroker(
    accounts=config['accounts'])

hmacmgr = HmacManager(accountmgr, app)

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

@app.route('/switch/<index>/test')
@hmac_auth("manage")
def test(index):
    board.test_switch(int(index))
    return "ok"

@app.route('/switches/test')
@hmac_auth("manage")
def test_all():
    board.test_switches()
    return "testing"

@app.route('/switches/on')
@hmac_auth("manage")
def on_all():
    board.turn_all_on()
    return "on"

@app.route('/switches/off')
@hmac_auth("manage")
def off_all():
    board.turn_all_off()
    return "off"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
