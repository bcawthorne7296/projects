import mcpi.minecraft as minecraft, time as t, random #imports time, random and minecraft and shortens in
mc = minecraft.Minecraft.create() #opens connection to current minecraft game

while True: #loops infinitely
    pos = mc.player.getPos() #gets players position
    x1 = float(pos.x + random.randint(-10,10)) #adds a random number between -10 and 10 to the players x position
    z1 = float(pos.z + random.randint(-10,10)) #adds a random number between -10 and 10 to the players z position
    mc.setBlock(x1, pos.y + 50, z1, 13) #makes blocks appear in the sky, 50 blocks above the player within a ten by ten square of him
    t.sleep(0.2)#pauses the program for 0.2 seconds
    
    
