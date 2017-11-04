import datetime
now = datetime.datetime.now()
name = now.strftime('%Y%m%d_%H%M%S.txt')
print name
