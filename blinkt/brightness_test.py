# Pyrthon script to test / show the different brightness levels of the Pimoroni Blinkt lights 

import math
import time

from blinkt import set_pixel, show

# define function for a float range
def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step

# great loop for brightness level
for i in frange(0.1, 1.0, 0.1):
    # use all eight lights, its in a loop, but there's no delay, so they all come on at once
    for x in range(0, 8):
        # turn on light, make it red and use options 5th parameter to set brightness
    	set_pixel(x,0,255,0,i)
    	show()
    # wait one second between brightness levels
    time.sleep(1.0)
