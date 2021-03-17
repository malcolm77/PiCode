#!/bin/bash

##########################################
#
# Take a series of timelapse images
#
#  --timeout   : Time (in ms) before takes picture and shuts down (if not specified, set to 5s)
#  --timelapse : Timelapse mode. Takes a picture every <t>ms. %d == frame number (Try: -o img_%04d.jpg)
#  --rotation        : Set image rotation (0, 90, 180, or 270)
#  --output    : Output filename <filename> (to write to stdout, use '-o -'). If not specified, no file is saved
#
# raspistill -t 30000 -tl 2000 -o image%04d.jpg
# Note the %04d in the output filename: this indicates the point in the filename where you want a frame count number to appear. 
# So, for example, the command above will produce a capture every two seconds (2000ms), 
# over a total period of 30 seconds (30000ms), 
# named image0001.jpg, image0002.jpg, and so on, through to image0015.jpg.
# 
# 8 hours is 28800000 milliseconds
# 10 minutes is 600000 milliseconds

raspistill --timeout 600000 --timelapse 2000 --rotation 180 --output images/image%08d.jpg
