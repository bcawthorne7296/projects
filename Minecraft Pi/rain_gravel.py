import mcpi.minecraft as minecraft, time as t, random #imports time, random and minecraft and shortens in
mc = minecraft.Minecraft.create() #opens connection to current minecraft game

while True: #loops infinitely
    pos = mc.player.getPos() #gets players position
    x = pos.x #declares vriable x and gives it the value of the players x co-ordinate
    y = pos.y #declares vriable y and gives it the value of the players y co-ordinate
    z = pos.z #declares vriable z and gives it the value of the players z co-ordinate
    x1 = float(x + random.randint(-10,10)) #adds a random number between -10 and 10 to the players x position
    z1 = float(z + random.randint(-10,10)) #adds a random number between -10 and 10 to the players z position
    mc.setBlock(x1, y + 50, z1, 13) #makes blocks appear in the sky, 50 blocks above the player within a ten by ten square of him
    t.sleep(0.2)#pauses the program for 0.2 seconds
    
    
