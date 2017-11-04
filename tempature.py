import subprocess

tempature = subprocess.Popen("echo $((`cat /sys/class/thermal/thermal_zone0/temp|cut -c1-2`)).$((`cat /sys/class/thermal/thermal_zone0/temp|cut -c3-5`))", shell=True, stdout=subprocess.PIPE).stdout.read()
lightval = subprocess.Popen("echo $((`cat /sys/class/thermal/thermal_zone0/temp`/10000))", shell=True, stdout=subprocess.PIPE).stdout.read()

print "temp is :", tempature 
print "temp value is :", lightval
