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
# 1 minute is 60000 milliseconds

DATE=$(date +"%Y-%m-%d_%H%M")
#raspistill -vf -hf -o $DATE.jpg

raspistill --timeout 28800000 --timelapse 60000 --output images/image%08d.jpg

ls images/*.jpg > stills.txt

mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o timelapse.mp4 -mf type=jpeg:fps=24 mf://@stills.txt
