import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Sensor:
    def __init__(self, pinNumber):
        GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.on_motion = None

        # Callback function to run when motion detected
        def motionSensor(channel):
            if GPIO.input(pinNumber):     # True = Rising
                print "Motion detected"
                if self.on_motion is not None:
                    self.on_motion()

        # add event listener on pin 21
        GPIO.add_event_detect(pinNumber, GPIO.BOTH, callback=motionSensor, bouncetime=300)