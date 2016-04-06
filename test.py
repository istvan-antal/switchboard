#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BOARD)

# init list with pin numbers

with open("config.json") as data_file:
    data = json.load(data_file)

# loop through pins and set mode and state to 'low'
GPIO.setup(pinList, GPIO.OUT)
GPIO.output(pinList, GPIO.HIGH)

GPIO.output(11, GPIO.LOW)

time.sleep(1)

GPIO.output(11, GPIO.HIGH)

time.sleep(3)

GPIO.cleanup()

# find more information on this script at
# http://youtu.be/oaf_zQcrg7g
