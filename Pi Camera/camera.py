import picamera,time #imports modules of the picamera and time

with picamera.PiCamera() as camera: #does the softwre inside the loop then deletes it
    camera.resolution = (1024,768) #sets camera resolution
    camera.start_preview() 

    time.sleep(2) #pauses for 2 seconds
    camera.capture("pictures.jpeg") #takes picture and calls it pictures.jpeg
