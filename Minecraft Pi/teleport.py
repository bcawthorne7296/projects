import time, mcpi.minecraft as minecraft, random #imports the modules of time and minecraft and the second module to be shorter
mc = minecraft.Minecraft.create() #opens connection with current minecraft game

time.sleep(3) #Pauses the program for 3 seconds

x = random.randint(0,256)
y = random.randint(0,256)
z = random.randint(0,256)

while True:
    mc.postToChat("Teleporting in...")#Posts message to chat

    #Counts down
    time.sleep(1)
    mc.postToChat("3")
    time.sleep(1)
    mc.postToChat("2")
    time.sleep(1)
    mc.postToChat("1")
    time.sleep(1)

    #Teleports player three times
    mc.player.setPos(x,y,z)
    time.sleep(2)
    mc.player.setPos(x,y,z)
    time.sleep(2)
    mc.player.setPos(0,0,0)
    time.sleep(2)
    mc.postToChat("Teleportation complete!")
    time.sleep(1)
