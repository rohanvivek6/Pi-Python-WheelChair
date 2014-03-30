import cwiid
import time
import led
def connect(Led):
	while True:
		try:	
			print 'Press Button 1 and 2 on the remote'
			led.on(Led)
			time.sleep(1)
			wm=cwiid.Wiimote()
		except RuntimeError:
			continue
		break
	print 'Remote Connected'
	led.off(Led)
	time.sleep(1)

	Rumble = False
	wm.rpt_mode=cwiid.RPT_BTN
	return wm
	
def whichbutton(wm):
	if(wm.state['buttons']==2):
		print'1'
		return (1)
	if(wm.state['buttons']==1):
		print'2'
		return(2)
	if(wm.state['buttons']==2048):
	        print'UP3'
		return(3)
        if(wm.state['buttons']==1024):
                print'Down4'
                return(4)
        if(wm.state['buttons']==256):
                print'Left2'
                return(5)
        if(wm.state['buttons']==512):
                print'6Right'
                return(6)
	if(wm.state['buttons']==128):
		print'7Home'
		return(7)
