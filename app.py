#!/usr/bin/python
from flask import Flask, jsonify
from flask.ext.hmacauth import DictAccountBroker, HmacManager
from hmac_auth import hmac_auth

from switchboard import SwitchBoard
import json
import desklamp
from pir import Sensor

sensor = Sensor(19, board, 0)

with open("config.json") as data_file:
    config = json.load(data_file)

board = SwitchBoard(config['switches'])
#if "desklamps" in config:
#    desklamp.load(board, config["desklamps"])

app = Flask(__name__)

accountmgr = DictAccountBroker(
    accounts=config['accounts'])

hmacmgr = HmacManager(accountmgr, app)

@app.route("/")
def home():
    return jsonify({
        "status": "ok"
    })

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
    context = ('switchboard.crt', 'switchboard.key')
    flask_config = {}

    if "flask" in config:
        flask_config = config["flask"]
        if "ssl_context" in flask_config:
            flask_config["ssl_context"] = (flask_config["ssl_context"][0], flask_config["ssl_context"][1])

    if "host" not in flask_config:
        flask_config["host"] = '0.0.0.0'

    if "debug" not in flask_config:
        flask_config["debug"] = True

    app.run(**flask_config)
