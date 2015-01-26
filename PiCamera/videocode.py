import picamera,RPi.GPIO as GPIO,time

button = 14
balloon = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(balloon, GPIO.OUT)

with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.framerate=(90)
    camera.start_recording('my_video2.h264')
    camera.wait_recording(5)
    

    print("Ready...")
    GPIO.wait_for_edge(button, GPIO.FALLING)
    GPIO.output(balloon,True)
    time.sleep(5)
    GPIO.output(balloon,False)
    print("Pop!")
    camera.wait_recording(20)
    camera.stop_recording()

