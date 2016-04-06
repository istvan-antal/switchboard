#!/usr/bin/python
from flask import Flask
from switchboard import SwitchBoard
import json

with open("config.json") as data_file:
    board = SwitchBoard(json.load(data_file)['pins'])

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
