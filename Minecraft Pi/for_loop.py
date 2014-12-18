#For loops in Python

import mcpi.minecraft as minecraft, time #imports modules
mc = minecraft.Minecraft.create() #connects to the minecraft game

#builds a block in the set location with the Y co-ordinate as the item in the list then posts the block's y co-ordinate to the chat
for block in (3,8):
    mc.setBlock(10,30,block,22)
    mc.postToChat(block)
    time.sleep(1)

#each name in the list will be posted to the chat in Minecraft with 1 second intervals
for name in ("Jo", "Tom", "Fred"):
    mc.postToChat(name)
    time.sleep(1)
