# import libraries
import math
import time
import subprocess
from blinkt import set_pixel, show

# get actual tempature
tempature = subprocess.Popen("echo $((`cat /sys/class/thermal/thermal_zone0/temp|cut -c1-2`)).$((`cat /sys/class/thermal/thermal_zone0/temp|cut -c3-5`))", shell=True, stdout=subprocess.PIPE).stdout.read()
# get first number of tempature
lightval = subprocess.Popen("echo $((`cat /sys/class/thermal/thermal_zone0/temp`/10000))", shell=True, stdout=subprocess.PIPE).stdout.read()

# convert string to int
temp = int(lightval)

# turn on number of light equal to value of first digit in temp 
# if value/temp is above 60 make lights red instead of green
# NOTE: 8 lights would equal a temp of 8 or 80 degress which is about the max temp it should be!
for x in range(0, temp):
    if temp >= 6:	
       set_pixel(x,255,0,0)
    else:
       set_pixel(x,0,255,0)
    show()
    time.sleep(0.1)

# sleep for 5 seconds to keep lights on
time.sleep(5.0)
