#Morse code runnere by Bethany

import RPi.GPIO as GPIO,time #Imports the time and GPIO so that I can control them later on
GPIO.setmode(GPIO.BOARD) #Sets the pin numbering system
GPIO.setup(11,GPIO.OUT) #Tells the Pi that I want the GPIO pin 11 to be output, not input

def dot():#dot will make it turn on then turn off quickly
	GPIO.output(11,True)
	time.sleep(0.5)#Pauses program for a second
	GPIO.output(11, False)
	time.sleep(0.75)

def dash():#dash will make the pi flash the led for longer than dot
	GPIO.output(11,True)
	time.sleep(1.5)
	GPIO.output(11, False)
	time.sleep(0.75)


def morse(letter):
	if letter == "a":
		dot()
		dash()
	elif letter == "b":
		dash()
		dot()
		dot()
		dot()
	elif letter == "c":
		dash()
		dot()
		dash()
	elif letter == "d":
		dash()
		dot()
		dot()
	elif letter == "e":
		dot()
	elif letter == "f":
		dot()
		dot()
		dash()
		dot()
	elif letter == "g":
		dash()
		dash()
		dot()
	elif letter == "h":
		dot()
		dot()
		dot()
		dot()
	elif letter == "i":
		dot()
		dot()
	elif letter == "j":
		dot()
		dash()
		dash()
		dash()
	elif letter == "k":
		dash()
		dot()
		dash()
	elif letter == "l":
		dot()
		dash()
		dot()
		dot()
	elif letter == "m":
		dash()
		dash()
	elif letter == "n":
		dash()
		dot()
	elif letter == "o":
		dash()
		dash()
		dash()
	elif letter == "p":
		dot()
		dash()
		dash()
		dot()
	elif letter == "q":
		dash()
		dash()
		dot()
		dash()
	elif letter == "r":
		dot()
		dash()
		dot()
	elif letter == "s":
		dot()
		dot()
		dot()
	elif letter == "t":
		dash()
	elif letter == "u":
		dot()
		dot()
		dash()
	elif letter == "v":
		dot()
		dot()
		dot()
		dash()
	elif letter == "w":
		dot()
		dash()
		dash()
	elif letter == "x":
		dash()
		dot()
		dot()
		dash()
	elif letter == "y":
		dash()
		dot()
		dash()
		dash()
		dash()
	elif letter == "z":
		dash()
		dash()
		dot()
		dot()
	else:
		print ("What is this? I don't understand!")
message = input("What message do you want? (without any spaces please :D)")

for each in message:
        morse(each)



