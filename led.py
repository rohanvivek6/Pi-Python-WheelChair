import RPi.GPIO as GPIO

def on(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,True)

def off(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,False)
def cleanup():
	GPIO.cleanup()
