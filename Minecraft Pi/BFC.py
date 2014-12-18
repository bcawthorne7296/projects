import mcpi.minecraft as minecraft, time as t, random #imports time, random and minecraft and shortens in
mc = minecraft.Minecraft.create() #opens connection to current minecraft game

pos = mc.player.getPos() #gets players position
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x-30,y-5,z-30,x+30,y+30,z+30,0) #Clears the area around the character

#Letter B
def b(x,y,z,colour)
    mc.setBlocks(x+2,y+6,z, x+2,y,z,35,colour)
    for line in (6,3,0):
        mc.setBlocks(x+3,y+line,z,x+5,y+line,z,35,colour)

    for dash in (5,4,2,1):
       mc.setBlock(x+6, y+dash,z,35,colour)

#Letter F
def f(x,y,z,colour):
    mc.setBlocks(x+8,y+6,z,x+8,y,z,35,colour)
    mc.setBlocks(x+9,y+6,z,x+12,y+6,z,35,colour)
    mc.setBlocks(x+9,y+3,z,x+11,y+3,z,35,colour)

#Letter C
def C(x,y,z,colour):
    mc.setBlocks(x+14,y+5,z,x+14,y+1,z,35,colour)
    for dash2 in (6,0):
        mc.setBlocks(x+15,y+dash2,z,x+17,y+dash2, z,35,colour)

    for dot in (5,1):
        mc.setBlock(x+18, y+dot,z,35,colour)

#Letter Q (unfinished)
def Q(x,y,z,colour):
    mc.setBlocks(x+2,y+1,z,x+2,y+7,z,35,colour)
    mc.setBlocks(x+6,y+2,z,x+6,y+7,z,35,colour)
    mc.setBlocks(x+3,y+8,z,x+5,y+8,z,35,colour)
    mc.setBlocks(x+3,y,z,x+4,y,z,35,colour)






    
    
