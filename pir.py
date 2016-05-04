try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
except ImportError:
    import fake_gpio as GPIO

GPIO.setmode(GPIO.BOARD)

class Sensor:
    def __init__(self, config):
        GPIO.setup(config["pinNumber"], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.on_motion = None

        # Callback function to run when motion detected
        def motionSensor(channel):
            if GPIO.input(config["pinNumber"]):     # True = Rising
                print "Motion detected"
                self.on_motion()

        # add event listener on pin 21
        GPIO.add_event_detect(config["pinNumber"], GPIO.BOTH, callback=motionSensor, bouncetime=300)