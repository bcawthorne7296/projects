import time, mcpi.minecraft as minecraft, random #imports the modules of time and minecraft and the second module to be shorter
mc = minecraft.Minecraft.create() #opens connection with current minecraft game

time.sleep(3) #Pauses the program for 3 seconds

pos = mc.player.getPos() #gets players position
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

mc.setBlocks(-127,-127,-127,127,127,127,0)

def build_house(x,y,z):
    mc.setBlocks(x+1, y+6, z+1, x+8, y+0, z+5, 1)
    mc.setBlocks(x+2, y+5, z+2, x+7, y+0, z+4, 0)
    mc.setBlocks(x+1,y+2,z+2,x+2,y,z+2,0)

time.sleep(3)
mc.player.setPos(10,30,20)
build_house(20,0,30)
build_house(50,0,30)
build_house(60,0,30)
build_house(40,0,30)
build_house(30,0,30)
build_house(20,0,20)
build_house(50,0,20)
build_house(60,0,20)
build_house(40,0,20)
build_house(30,0,20)
build_house(20,0,40)
build_house(50,0,40)
build_house(60,0,40)
build_house(40,0,40)
build_house(30,0,40)








    


