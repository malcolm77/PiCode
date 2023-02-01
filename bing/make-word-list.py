import random
import linecache

a=random.randint(1,178186)

print(a)

word = linecache.getline(r"words.txt",a)
print (word)


f = open("/var/www/html/words.html", "w")

f.write ("<html>")
f.write ("<head>")
f.write ("<link rel='stylesheet' href='words.css'>")
f.write ("</head>")


f.write ("<body>")
for i in range(60):
  a=random.randint(1,178186)
  word = linecache.getline(r"words.txt",a)
  print (word)
  f.write("<a href='http://www.bing.com/search?q="+word+"'>"+str(i)+" "+word+"</a><br>")
  i=i+1

f.write ("<HR>")
f.write ("</body>")
f.write ("</html>")
f.close()
