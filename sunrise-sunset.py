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

#print ("Test Data")
#print (prev_sunset.strftime("%d/%m/%Y %H:%M:%S"))
#print (next_sunrise.strftime("%d/%m/%Y %H:%M:%S"))
#print ("Sunset is at " + prev_sunset.strftime("%I:%M%p %A the %d of %B "))

f = open("/var/www/html/sunrise.html", "w")
f.write("<h1 style=color:White>")
f.write("<table style=color:White>")
f.write("<tr><td>Sunset</td>" + prev_sunset.strftime("<td>%I:%M%p</td><td>%A</td><td>%d of %B</td></tr>"))
#f.write("<br>")
f.write("<tr><td>Sunrise</td>" + next_sunrise.strftime("<td>%I:%M%p</td><td>%A</td><td>%d of %B</td><td></tr>"))
f.write("</table>")
f.write("</h1>")
f.close()
