#For loops in Python

import mcpi.minecraft as minecraft, time #Imports the modules minecraft and time
mc = minecraft.Minecraft.create() #Opens connection with the current minecraft game

mc.setBlocks(-30,-5,-30,30,30,30,0) #Clears the area around the character

for base in range(5): #For each item in this list, it will build  block with that block id in a tower
    mc.setBlocks(base,0,5-base,35,4) #This is the location that the block will be. The b for the y coordinate means it will go up one each time and the b for the block id means it will keep changing block type
    time.sleep(0.01) #Pauses program
    

    










