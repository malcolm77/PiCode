import ephem
import datetime

Canberra=ephem.Observer()
Canberra.lat='-35.246669'
Canberra.lon='149.070136'
Canberra.date = datetime.datetime.now()
Canberra.elevation = 605

sun = ephem.Sun()

prev_sunrise = ephem.localtime(Canberra.previous_rising(sun))
prev_sunset = ephem.localtime(Canberra.previous_setting(sun))
next_sunrise = ephem.localtime(Canberra.next_rising(sun))
next_sunset = ephem.localtime(Canberra.next_setting(sun))

print "Date"
print (datetime.datetime.now())
print (Canberra.date)
print "Yesterday"
print prev_sunrise.strftime("%d/%m/%Y %H:%M:%S")
print prev_sunset.strftime("%d/%m/%Y %H:%M:%S")
print "Today"
print next_sunrise.strftime("%d/%m/%Y %H:%M:%S")
print next_sunset.strftime("%d/%m/%Y %H:%M:%S")
