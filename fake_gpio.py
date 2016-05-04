def setup(*arg):
    print "GPIO.setup(" + str(arg) + ")"

def cleanup(*arg):
    print "GPIO.cleanup(" + str(arg) + ")"

def output(*arg):
    print "GPIO.output(" + str(arg) + ")"

def setmode(*arg):
    print "GPIO.setmode(" + str(arg) + ")"

OUT = 'GPIO.OUT'
HIGH = 'GPIO.HIGH'
LOW = 'GPIO.LOW'
BOARD = 'GPIO.BOARD'
IN = 'GPIO.IN'
PUD_DOWN = 'GPIO.PUD_DOWN'