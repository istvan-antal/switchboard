import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Sensor:
    def __init__(self, pinNumber, board, switchPinIndex):
        GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Callback function to run when motion detected
        def motionSensor(channel):
            if GPIO.input(pinNumber):     # True = Rising
                print "Motion detected"
                board.turn_on(switchPinIndex)

        # add event listener on pin 21
        GPIO.add_event_detect(pinNumber, GPIO.BOTH, callback=motionSensor, bouncetime=300)