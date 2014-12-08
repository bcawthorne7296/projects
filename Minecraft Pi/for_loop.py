#For loops in Python

import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

for block in (3,8):
    mc.setBlock(10,30,block,22)
    mc.postToChat(block)
    time.sleep(1)


for name in ("Jo", "Tom", "Fred"):
    mc.postToChat(name)
    time.sleep(1)
