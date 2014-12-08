import mcpi.minecraft as minecraft, time as t #imports minecraft pi and time modules and renmes them to shortenn them
mc = minecraft.Minecraft.create() #starts connection with minecraft game

#moves player closer to origin
mc.player.setPos(-9.7,6.5,0.9)

black=7
red=14
orange=1
green=5

#set up empty lights
mc.setBlock(0,0,0,35,black)
mc.setBlock(0,1,0,35,black)
mc.setBlock(0,2,0,35,black)
mc.setBlock(0,3,0,35,black)
mc.setBlock(0,4,0,35,black)
mc.setBlock(0,5,0,35,black)

while True: #loops program
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,5,0,35,red)
    t.sleep(10)
    mc.setBlock(0,4,0,35,orange)
    t.sleep(3)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,3,0,35,green)
    t.sleep(10)
    mc.setBlock(0,3,0,35,black)
    mc.setBlock(0,4,0,35,orange)
    t.sleep(4)
