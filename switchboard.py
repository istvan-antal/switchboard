import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class SwitchBoard:
    def __init__(self, pinList):
        self._pinList = pinList
        self.reset()
        self.test_switch(6)

        GPIO.cleanup()

    def test_switch(self, index):
        pinNumber = self._pinList[index]
        GPIO.output(pinNumber, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pinNumber, GPIO.HIGH)

        time.sleep(3)

    def reset(self):
        # loop through pins and set mode and state to 'low'
        GPIO.setup(self._pinList, GPIO.OUT)
        GPIO.output(self._pinList, GPIO.HIGH)
