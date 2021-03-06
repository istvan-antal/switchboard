import time

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
except ImportError:
    import fake_gpio as GPIO

class SwitchBoard:

    def __init__(self, pinList):
        self._pinList = pinList
        self.reset()

    def test_switches(self):
        indexes = range(0, self._count())
        for i in indexes:
            self.turn_on(i)
            time.sleep(1)

        for i in reversed(indexes):
            self.turn_off(i)
            time.sleep(1)

    def test_switch(self, index):
        self.turn_on(index)
        time.sleep(1)
        self.turn_off(index)

    def turn_all_on(self):
        indexes = range(0, self._count())
        for i in indexes:
            self.turn_on(i)

    def turn_all_off(self):
        indexes = range(0, self._count())
        for i in indexes:
            self.turn_off(i)

    def turn_on(self, index):
        GPIO.output(self._get_pin_number(index), GPIO.LOW)

    def turn_off(self, index):
        GPIO.output(self._get_pin_number(index), GPIO.HIGH)

    def _get_pin_number(self, index):
        return self._pinList[index]

    def _count(self):
        return len(self._pinList)

    def reset(self):
        # TODO: add GPIO.gpio_function checks
        GPIO.setup(self._pinList, GPIO.OUT)
        GPIO.output(self._pinList, GPIO.HIGH)

    def __del__(self):
        GPIO.cleanup()
