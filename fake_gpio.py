def setup(*arg):
    print "GPIO.setup(" + str(arg) + ")"

def cleanup(*arg):
    print "GPIO.cleanup(" + str(arg) + ")"

def output(*arg):
    print "GPIO.output(" + str(arg) + ")"

OUT = 'GPIO.OUT'
HIGH = 'GPIO.HIGH'
