import RPi.GPIO as GPIO, time #imports the modules GPIO and time
GPIO.setmode(GPIO.BCM) #tells the pi what numbering system the code is running on

TRIG = 14
ECHO = 23

print("Distance measurement in process")

GPIO.setup(TRIG,GPIO.OUT) #tells the pi that TRIG(pin 23) is an output
GPIO.setup(ECHO,GPIO.IN) #tells the pi that ECHO (pin 24) is an input

GPIO.output(TRIG, False) #turns off pin 23
print("Waiting for sensor to settle")
time.sleep(2) #pauses for 2 seconds

while True:
	GPIO.output(TRIG,True) #turns on pin 23
	time.sleep(0.00001)
	GPIO.output(TRIG, False) #turns off pin 23

	while GPIO.input(ECHO)==0: #when ECHO has recieved no input, it starts the timer
		pulse_start = time.time()

	while GPIO.input(ECHO)==1: #when ECHO has recieved the input from the pulse returning, it stops the timer
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start #calculates how long it took for the pulse to return

	distance = pulse_duration * 17150 #converts the data from time to distance

	distance = round(distance,2) #rounds the distance to two decimal places

	print("Distance:",distance, " cm") #prints how far away the object is

	time.sleep(2)
