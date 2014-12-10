import RPi.GPIO as GPIO, time as t
GPIO.setmode(GPIO.BOARD)

#sets up pins as outputs
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

fwd_l = GPIO.PWM(21, 50)
bwd_l = GPIO.PWM(23, 50)
fwd_r = GPIO.PWM(24, 50)
bwd_r = GPIO.PWM(26, 50)

def fwd(pwr, dur): #function to make the robot drive forward
    fwd_r.start(pwr)
    fwd_l.start(pwr)
    t.sleep(dur)
    fwd_l.stop()
    fwd_r.stop()

def bwd(pwr, dur): #function to make the robot reverse
    bwd_l.start(pwr)
    bwd_r.start(pwr)
    t.sleep(dur)
    bwd_l.stop()
    bwd_r.stop()

def anticlockwise(pwr, dur): #function to make the robot turn left
    fwd_r.start(pwr)
    bwd_l.start(pwr)
    t.sleep(dur)
    fwd_r.stop()
    bwd_l.stop()

def clockwise(pwr, dur): #function to make the robot turn right
    fwd_l.start(pwr)
    bwd_r.start(pwr)
    t.sleep(dur)
    fwd_l.stop()
    bwd_r.stop()

def stop(): #function to stop the robot moving
    fwd_l.stop()
    bwd_l.stop()
    fwd_r.stop()
    bwd_r.stop()


