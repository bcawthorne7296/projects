import mcpi.minecraft as minecraft, time #imports minecraft and time
mc = minecraft.Minecraft.create() #opens connection to current minecraft game

while True: #infinate loop
    pos = mc.player.getPos() #gets players position
    x = pos.x
    y = pos.y
    z = pos.z
    gold = 41 #defines the variable gold to it's block value
    mc.setBlock(x, y, z, gold) #turns the block that the player is touching to gold
    time.sleep(0.2) #pauses program
