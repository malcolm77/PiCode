# Blinkt Function Reference
# The two Blinkt methods you'll most commonly use are `set_pixel` and `show`. Here's a simple example:

import math
import time

from blinkt import set_pixel, show
# set_pixel(4,0,255,0)
# show()

# `set_pixel` takes an optional fifth parameter; the brightness from 0.0 to 1.0.
# 
# `set_pixel(pixel_no, red, green, blue, brightness)`
# 
# You can also change the brightness with `set_brightness` from 0.0 to 1.0, for example:

# from blinkt import set_brightness
# 
# set_brightness(0.5)
# show()

for x in range(0, 8):
    set_pixel(x,0,255,0)
    show()
    time.sleep(0.1)
