print("Hello")
import RPi.GPIO as GPIO, time, motor_control as mc #imports the modules GPIO and time
from threading import Thread
GPIO.setmode(GPIO.BCM) #tells the pi what numbering system the code is running on
GPIO.setwarnings(False)

TRIG = 14
ECHO = 23

print("Distance measurement in process")

GPIO.setup(TRIG,GPIO.OUT) #tells the pi that TRIG(pin 14) is an output
GPIO.setup(ECHO,GPIO.IN) #tells the pi that ECHO (pin 23) is an input

GPIO.output(TRIG, False) #turns off pin 14
print("Waiting for sensor to settle")
time.sleep(2) #pauses for 2 seconds

distance = 100000000

def sense():
        global distance
        while True: #potentially infinite loop
                time.sleep(0.1)
                GPIO.output(TRIG,True)#turns on pin 14
                time.sleep(0.00001)
                GPIO.output(TRIG, False) #turns off pin 14

                while GPIO.input(ECHO)==0: #when ECHO equals zero, it starts the timer
                        pulse_start = time.time()
                #print(pulse_start)

                while GPIO.input(ECHO)==1: #when ECHO has recieved the input from the pulse returning, it stops the timer
                        pulse_end = time.time()
                #print(pulse_end)

                pulse_duration = pulse_end - pulse_start #calculates how long it took for the pulse to return

                distance = pulse_duration * 17150 #converts the data from time to distance

                distance = round(distance,2) #rounds the distance to two decimal places

                print("Distance:",distance, " cm") #prints how far away the object is


def move(): #this function will control the robot's movement
        global distance
        #the following instructions control how fast the robot moves, dependingon the distance away from the nearest object
        while distance >= 5:
                if distance >= 15:
                        mc.fwd(100,0.5)
                elif distance >= 8:
                        mc.fwd(50,0.5)
                elif distance >= 5:
                        mc.stop()
                        GPIO.cleanup()
                else:
                        ultrasonic.stop()
                        mc.stop()
                        drive.stop()

try: #here a new thread is started so at the same time the robot can judge distance and drive
    ultrasonic=Thread( target=sense,args=())
    ultrasonic.start()
    drive =Thread(target=move,args=())
    drive.start()
except: #if the thread is unable to run, it will print an error message
    print("There was an error running the threads")


        
                        
                        

                
