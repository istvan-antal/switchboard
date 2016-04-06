import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class SwitchBoard:

    def __init__(self, pinList):
        self._pinList = pinList
        self.reset()

    def test_switch(self, index):
        self.turn_on(index)
        time.sleep(1)
        self.turn_off(index)

    def turn_on(self, index):
        GPIO.output(self._get_pin_number(index), GPIO.LOW)

    def turn_off(self, index):
        GPIO.output(self._get_pin_number(index), GPIO.HIGH)

    def _get_pin_number(self, index):
        return self._pinList[index]

    def reset(self):
        GPIO.setup(self._pinList, GPIO.OUT)
        GPIO.output(self._pinList, GPIO.HIGH)

    def __del__(self):
        print "cleanup"
        GPIO.cleanup()
