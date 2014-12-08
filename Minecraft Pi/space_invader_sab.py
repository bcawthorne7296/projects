import time as t, mcpi.minecraft as minecraft #imports the modules of time and minecraft and then shortens them
mc = minecraft.Minecraft.create() #opens connection with current minecraft game

t.sleep(3) #Pauses the program for 3 seconds

pos = mc.player.getPos() #gets players position
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

#defines colours
orange = 1
magenta = 2
blue = 3
yellow = 4
green = 5
pink = 6
gray = 8
cyan = 9
purple = 10
brown = 12
red = 14
black = 15

def space_invader(x,y,z,colour,time):
    while True: #loops infinitely so the space invader will keep changing apperence
        #builds space invader
        mc.setBlocks(x+20,y+20,z+20,x,y,z,0)#clears area
    
        for row1 in (3,9): #For each item in this list, it will build  block 
            mc.setBlock(x+row1,y+19,z+10,35,colour) #This is the location that the block will be

        for row2 in (4,8): #For each item in this list, it will build  block 
            mc.setBlock(x+row2,y+18,z+10,35,colour) #This is the location that the block will be
    
        mc.setBlocks(x+1,y+20,z+10,x+11,y+13,z+10,35,colour)#Builds a rectangle to make the basic body of the space invader

        for row3 in (1,2,10,11):
            mc.setBlock(x+row3,y+17,z+10,0)

        for row4 in (1,4,8,11):
            mc.setBlock(x+row4,y+15,z+10,0)
    
        for row5 in (2,10):
            mc.setBlock(x+row5,y+14,z+10,0)

        for row6 in (2,4,5,6,7,8,10):
            mc.setBlock(x+row6,y+13,z+10,0)

        for row7 in (4,5,7,8):
            mc.setBlock(x+row7,y+12,z+10,35,colour)

        t.sleep(time)#pauses program
        
        mc.setBlocks(x+20,y+20,z+20,x,y,z,0)#removes past space invader and replaces it with the new space invader appearence

        #second space invader shape
        for row8 in (3,9): #For each item in this list, it will build  block 
            mc.setBlock(x+row8,y+19,z+10,35,colour) #This is the location that the block will be

        for row9 in (4,8): 
            mc.setBlock(x+row9,y+18,z+10,35,colour) 

        mc.setBlocks(x+1,y+17,z+10,x+11,y+13,z+10,35,colour)

        for row10 in (2,3,9,10):
            mc.setBlock(x+row10,y+18,z+10,0)

        for row11 in (2,10):
            mc.setBlock(x+row11,y+17,z+10,0)
    
        for row12 in (4,8):
            mc.setBlock(x+row12,y+16,z+10,0)

        for row13 in (1,11):
            mc.setBlock(x+row13,y+13,z+10,0)

        for row14 in (3,9):
            mc.setBlock(x+row14,y+12,z+12,35,colour)

        for row15 in (2,10):
            mc.setBlock(x+row15,y+11,z+10,35,colour)

        for row16 in (2,10):
            mc.setBlock(x+row16,y+16,z+10,35)

        t.sleep(time)#pauses the program

space_invader(x,y,z,purple,0.5) #calls function




    


