import RPi.GPIO as GPIO, time as t, motor_control as mc
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = [7,8,10,11,12] #creates a list so I can easily refer to the pins

for pin in pins: 
        GPIO.setup(pin,GPIO.IN,GPIO.PUD_UP) #sets all pins as inputs, and tells the program to round up the value they read
state = [0,0,0,0,0]

while True:
        for ir in range(5):
                state[ir] = (GPIO.input(pins[ir])) #changes the state depending on the values the IR sensors are reading
        t.sleep(0.1)
        print(state)
        if state[0] + state[1] + state[2] > state[2] + state[3] + state[4]: #finds the average of the values 
                mc.clockwise(100,0.35) #If the sensors on the lefts value's are higher than the values on the right, it will turn clockwise and it'll turn the other way if the right side is higher
        elif state[0] + state[1] + state[2] < state[2] + state[3] + state[4]:
                mc.anticlockwise(100,0.35)
        else:
                mc.fwd(100,0.5) #if each sensor is recording the same value then it'll drive forward
        
        

                        





