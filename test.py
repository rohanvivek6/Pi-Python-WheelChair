import wimote
import cwiid
import time
import usonic
import led
import motor
import sys
Trigger_front = 8
Echo_front = 7
Collision=10
Led=11
def main():
	wm=wimote.connect(Led)
	while True:
		button=wimote.whichbutton(wm)
		time.sleep(0.05)
		wm.rumble=False
	
			
		#Moving Forwards		
		if button==3:
			distance_front = usonic.reading(Trigger_front,Echo_front)
			print distance_front
			if distance_front < Collision:
				wm.rumble=True
				#led.off(Led)
				motor.stop()
			elif distance_front >= Collision:
				#led.on(Led)
				motor.forward()
		#Reverse
		if button==4:
			motor.reverse()
		if button==7:
			motor.cleanup()
			led.cleanup()
			usonic.cleanup()
			sys.exit()
		if button==None:
			led.off(Led)
			motor.stop()

if __name__=="__main__":
	main()
