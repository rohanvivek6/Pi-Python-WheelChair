import RPi.GPIO as GPIO # always needed with RPi.GPIO  
  
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM    
GPIO.setup(9, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port  
GPIO.setup(10, GPIO.OUT)
  
p = GPIO.PWM(9, 50)
q = GPIO.PWM(10, 50)

def forward():
	q.stop()
	p.start(50)

def stop():
	p.stop()
	q.stop()

def reverse():
	p.stop()
	q.start(50)

def cleanup():
	GPIO.cleanup()
