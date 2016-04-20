import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Callback function to run when motion detected
def motionSensor(channel):
    if GPIO.input(19):     # True = Rising
        print "motion detected"

# add event listener on pin 21
GPIO.add_event_detect(19, GPIO.BOTH, callback=motionSensor, bouncetime=300)