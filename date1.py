from datetime import date,datetime
d=date(1993,7,19)
print(d.ctime())
print(d.replace(1993,2,19))
print(d.isoformat())
print(d.isoweekday())
print(d.weekday())
print(d.strftime("%m-%d-%y"))
print(d.timetuple())
print(d.toordinal(),d.fromordinal(d.toordinal()))
d1=datetime.now()
print(d1)
d2=datetime.today()
print(d2)
#print(d2.strptime())
#print(timedelta(d,d1))
