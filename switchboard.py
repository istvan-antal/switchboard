import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class SwitchBoard:

    def __init__(self, pinList):
        self._pinList = pinList
        self.reset()
        
    def test_switch(self, index):
        pinNumber = self._pinList[index]
        GPIO.output(pinNumber, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pinNumber, GPIO.HIGH)

    def reset(self):
        GPIO.setup(self._pinList, GPIO.OUT)
        GPIO.output(self._pinList, GPIO.HIGH)

    def __del__(self):
        print "cleanup"
        GPIO.cleanup()
