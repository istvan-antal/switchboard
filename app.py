#!/usr/bin/python
from flask import Flask, abort, request, jsonify
from flask.ext.hmacauth import DictAccountBroker, HmacManager
from functools import update_wrapper

from switchboard import SwitchBoard
import json
import time
from desklamp import DeskLamp

with open("config.json") as data_file:
    config = json.load(data_file)

board = SwitchBoard(config['switches'])
if "desklamps" in config:
    desklamps = []
    for desklamp_config in config["desklamps"]:
        desklamps.append(DeskLamp(
            board=board,
            switchIndex=desklamp_config["switchIndex"],
            lat=float(desklamp_config["location"]["lat"]),
            long=float(desklamp_config["location"]["long"])
        ))

app = Flask(__name__)

accountmgr = DictAccountBroker(
    accounts=config['accounts'])

hmacmgr = HmacManager(accountmgr, app)

def hmac_auth(rights=None):
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if app.hmac_manager.is_authorized(request, rights):
                return f(*args, **kwargs)
            else:
                # TODO: make this custom,
                # maybe a current_app.hmac_manager.error() call?
                app.logger.info("hmac_auth failure")
                abort(403)
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/")
def home():
    return jsonify({
        "time": str(int(time.time())),
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
    app.run(debug=True, host='0.0.0.0')
