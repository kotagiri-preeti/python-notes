import calendar
cal= calendar.Calendar()
for x in cal.itermonthdates(2019,3):
    print(x)
print(cal.yeardatescalendar(2016, 3))
