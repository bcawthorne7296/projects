import picamera,time #imports modules of the picamera and time

def getPicture(name="Error"):
    try:
        check = False
        while check == False:
            with picamera.PiCamera() as camera: #does the softwre inside the loop then deletes it
                camera.resolution = (1024,768) #sets camera resolution
                camera.start_preview() 
                time.sleep(2) #pauses for 2 seconds
                filename = "{0}.jpeg".format(name)
                camera.capture(filename) #takes picture and calls it pictures.jpeg
                camera.stop_preview()
                response = input("Are you happy with your picture(Y/N)")
            if response == "Y":
                check=True
            elif response == "y":
                check=True
    except picamera.exc.PiCameraMMALError:
        print("There is an error with the camera. Please check it is connected correctly")
        filename = ""
    except picamera.exc.PiCameraError:
         print("Please ensure you have stated your name in speech marks in the brackets.")
         filename = ""
    return filename

def getCharProfile():
    name = ""
    while name == "":
        name = input("What is your name?")
        if input("Is your name " + name + "?(Y/N)").lower() == "y":
            getPicture(name)
        else:
            name=""
    hairResponse = ""
    while hairResponse=="":
        hairResponse = input("What colour is your hair?")
    hatResponse = ""
    while hatResponse=="":
        hatResponse = input("Are you wearing a hat(Y/N)?")
        if hatResponse.lower() == "y":
            hatResponse = True
        else:
            hatResponse = False
    eyeResponse = ""
    while eyeResponse=="":
        eyeResponse = input("What colour are your eyes?")
    genderResponse = ""
    while genderResponse=="":
        genderResponse = input("Are you male or female?")
    facialResponse = ""
    while facialResponse=="":
        facialResponse = input("Do you have facial hair(Y/N)?")
        if facialResponse.lower() == "y":
            facialResponse = True
        else:
            facialResponse = False
    glassesResponse = ""
    while glassesResponse=="":
        glassesResponse = input("Are you wearing glasses(Y/N)?")
        if glassesResponse.lower() == "y":
            glassesResponse = True
        else:
            glassesResponse = False
    return [name,hairResponse,hatResponse,eyeResponse,genderResponse,facialResponse,glassesResponse]
    
    
    

    
    
    
        

    
            

