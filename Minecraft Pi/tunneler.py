import mcpi.minecraft as minecraft #imports minecraft and shortens in
mc = minecraft.Minecraft.create() #opens connection to current minecraft game

import time

while True: #infinate loop
    pos = mc.player.getPos() #gets players position
    x = pos.x
    y = pos.y
    z = pos.z
    gold = 41 #defines the variable gold to it's block value
    mc.setBlocks(x, y, z, x + 2, y +3, z+2, 0) #turns the block that the player is touching to gold
    time.sleep(0.2) #pauses program
