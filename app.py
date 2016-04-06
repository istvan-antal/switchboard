#!/usr/bin/python
from switchboard import SwitchBoard
import json

with open("config.json") as data_file:
    board = SwitchBoard(json.load(data_file)['pins'])

board.test_switch(0)
