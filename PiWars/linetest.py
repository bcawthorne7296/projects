import RPi.GPIO as GPIO, time as t, motor_control
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.IN,GPIO.PUD_UP)

while True:
    val = GPIO.input(7)
    print(val)
    t.sleep(1)
