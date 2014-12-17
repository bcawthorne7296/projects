import picamera,time,json #imports modules of the picamera and time

def getPicture(name="Error"): #defines function for getting picture. If they don't provide a name, the picture will be saved as 'error'
    try:
        check = False
        while check == False:
            with picamera.PiCamera() as camera: #does the softwre inside the loop then deletes it
                camera.resolution = (1024,768) #sets camera resolution
                camera.start_preview() #displays picture preview
                time.sleep(2) #pauses for 2 seconds
                filename = "{0}.jpeg".format(name)
                camera.capture(filename) #takes picture and calls it pictures.jpeg
                camera.stop_preview() #stops showing the preview
                response = input("Are you happy with your picture(Y/N)")
            if response.lower() == "y": #If they re happy with the picture, the program will end. If not, it'll repeat
                check=True
    
    except picamera.exc.PiCameraMMALError: #if the camera isn't connected, it will tell the user instead of sending out an error
        print("There is an error with the camera. Please check it is connected correctly")
        filename = ""
    except picamera.exc.PiCameraError:#if the user hasn't stated the right parameters, itr will get the user to try again
         print("Please ensure you have stated your name in speech marks in the brackets.")
         filename = ""
    return filename

def getCharProfile():#defines a function for collecting someone's characteristics
    name = ""
    while name == "":#the loops will repeat until the person enters something
        name = input("What is your name?")
        if input("Is your name " + name + "?(Y/N)").lower() == "y": #checks if the name given is correct
            getPicture(name) #takes picture and saves it with the name of the person that they provided
        else:
            name=""
    hairResponse = ""
    while hairResponse=="": 
        hairResponse = input("What colour is your hair?")
    hatResponse = ""
    while hatResponse=="":
        hatResponse = input("Are you wearing a hat(Y/N)?")
        if hatResponse.lower() == "y":
            hatResponse = True#if the person is wearing a hat, it sets hat to true
        else:
            hatResponse = False #if the person isn't wearing a hat, it sets hat to false
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
    profileList = [name,hairResponse,hatResponse,eyeResponse,genderResponse,facialResponse,glassesResponse]#returns all the persons characteristics
    return profileList

def saveProfile(profiles):
    profile = getCharProfile()
    profiles.append(profile)
    with open("profiles.txt",mode="w") as my_file:
        json.dump(profiles,my_file)
    return profiles
def loadProfile():
    try:
        with open("profiles.txt",mode="r") as my_file:
            profiles = json.load(my_file)
            print(profiles)
    except IOError:
        print("Error")
        profiles = []
    return profiles










######Test
print("Hi")
profiles = loadProfile()
while len(profiles)<24:
    print("Hi2")
    profiles = saveProfile(profiles)
print("Hi3")
    

