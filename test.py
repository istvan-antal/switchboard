#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# init list with pin numbers

pinList = [3, 5, 7, 11, 13, 15, 16, 18]

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
