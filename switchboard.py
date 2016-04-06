import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class SwitchBoard:
    def __init__(self, pinList):
        # loop through pins and set mode and state to 'low'
        GPIO.setup(pinList, GPIO.OUT)
        GPIO.output(pinList, GPIO.HIGH)

        GPIO.output(11, GPIO.LOW)

        time.sleep(1)

        GPIO.output(11, GPIO.HIGH)

        time.sleep(3)

        GPIO.cleanup()
