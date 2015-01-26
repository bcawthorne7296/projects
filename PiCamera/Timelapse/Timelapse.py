import time, picamera #imports the modules for the picamera and time

with picamera.PiCamera() as camera:
    camera.start_preview() #starts preview of the picture it will take
    time.sleep(2) #pauses program for two seconds
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(5) #pauses program for 5 seconds
        
