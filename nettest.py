import os
address = "192.168.1.1"

ret = os.system("ping -c 3 -w 3000 " + address)
if ret != 0:
    print "alive"
