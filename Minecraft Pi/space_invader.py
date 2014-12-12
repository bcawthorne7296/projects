import time as t, mcpi.minecraft as minecraft, random #imports the modules of time and minecraft and then shortens them
mc = minecraft.Minecraft.create() #opens connection with current minecraft game

t.sleep(3) #Pauses the program for 3 seconds

pos = mc.player.getPos() #gets players position
x1 = int(pos.x)
y1 = int(pos.y)
z1 = int(pos.z)


def space_invader(x,y,z,colour,time):
    while True: #loops infinitely so the space invader will keep changing apperence
        #builds space invader
        mc.setBlocks(x+20,y+20,z+20,x,y,z,0)#clears area
    
        for row1 in (3,9): #For each item in this list, it will build  block 
            mc.setBlock(x+row1,y+19,z+10,35,colour) #This is the location that the block will be

        for row2 in (4,8): #For each item in this list, it will build  block 
            mc.setBlock(x+row2,y+18,z+10,35,colour) #This is the location that the block will be
    
        mc.setBlocks(x+1,y+17,z+10,x+11,y+13,z+10,35,colour)#Builds a rectangle to make the basic body of the space invader
        #creates details for the space invader by setting/removing blocks
        for row3 in (1,2,10,11):
            mc.setBlock(x+row3,y+17,z+10,0)

        for row4 in (1,4,8,11):
            mc.setBlock(x+row4,y+16,z+10,0)
    
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
            mc.setBlock(x+row14,y+12,z+10,35,colour)

        for row15 in (2,10):
            mc.setBlock(x+row15,y+11,z+10,35,colour)

        for row16 in (2,10):
            mc.setBlock(x+row16,y+16,z+10,0)

        t.sleep(time)#pauses the program

x = int(raw_input("Where do you want the space invader to be (x co-ordinte)?"))
#if the chosen x co-ordinate is in the minecraft world's boundaries, it will allow the block to be placed there
if -128 <= x <= 128:
    print("That will be the x co-ordinate.")
#if the chosen x co-ordinate is not in the minecraft world's boundaries, it will select a random location to place the block
else:
    x = x1
    print("I did not understand that. I will place the invader near the player.")

y = int(raw_input("Where do you want the space invader to be (y co-ordinate)?"))
#if the chosen y co-ordinate is in the minecraft world's boundaries, it will allow the block to be placed there
if -128 <= y <= 128:
    print("Tht will be the y co-ordinate")
#if the chosen x co-ordinate is not in the minecraft world's boundaries, it will select a random location to place the block
else:
    y = y1
    print("I did not understand that. I will place the invader near the player.")

z = int(raw_input("Where do you want the space invader to be (z co-ordinate)?"))
#if the chosen x co-ordinate is in the minecraft world's boundaries, it will allow the block to be placed there
if -128 <= z <= 128:
    print("That will be the z co-ordinate")
#if the chosen x co-ordinate is not in the minecraft world's boundaries, it will select a random location to place the block
else:
    z = z1
    print("I did not understand that. I will place the invader near the player.")

#defines colours
colour = raw_input("What colour do you want your invader to be?")
#depending on the colour entered, the pi will convert it into a number which will be the block id for the corresponding colour
if colour == "orange":
          colour = 1
elif colour == "magenta":
          colour = 2
elif colour == "blue":
          colour = 3
elif colour == "yellow":
          colour = 4
elif colour == "green":
          colour = 5
elif colour == "pink":
          colour = 6
elif colour == "gray":
          colour = 8
elif colour == "purple":
          colour = 10
elif colour == "brown":
          colour = 12
elif colour == "red":
          colour = 14
elif colour == "black":
          colour = 15
else: #if the user inputs a colour that is not known to the pi, it will select a random colour for the space invader
          print("Choosing random colour")
          colour = float(random.randint(1,15))
#gets the user to choose how fast they want the invader to move
time = float(raw_input("How fast do you want the space invader to move (put a number for the speed, the higher the number, the slower it moves"))


space_invader(x,y,z,colour,time) #calls function




    


