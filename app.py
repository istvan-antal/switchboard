#!/usr/bin/python
from flask import Flask
from switchboard import SwitchBoard
import json

with open("config.json") as data_file:
    board = SwitchBoard(json.load(data_file)['pins'])

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/switch/<index>/on')
def turn_on(index):
    board.turn_on(int(index))

@app.route('/switch/<index>/off')
def turn_off(index):
    board.turn_off(int(index))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
