#SOS flasher by Bethany


import RPi.GPIO as GPIO,time #Imports the time and GPIO so that I can control them later on
GPIO.setmode(GPIO.BOARD) #Sets the pin numbering system
GPIO.setup(11,GPIO.OUT) #Tells the Pi that I want the GPIO pin 11 to be output, not input

def dot():#dot will make it turn on then turn off quickly
	GPIO.output(11,True)
	time.sleep(1)#Pauses program for a second
	GPIO.output(11, False)
	time.sleep(0.75)

def dash():#dash will make the pi flash the led for longer than dot
	GPIO.output(11,True)
	time.sleep(3)
	GPIO.output(11, False)
	time.sleep(0.75)

#SOS in morse code
dot()
dot()
dot()
dash()
dash()
dash()
dot()
dot()
dot()


