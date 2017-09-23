from datetime import datetime

byear = input("What year were you born? [YYYY]: ")
bmonth = input("What month were you born? [MM]: ")
bday = input("What day were you born? [DD]: ")

dt = datetime(year = byear, month = bmonth, day = bday)
birthday = datetime.strftime(dt, '%d/%m/%Y')
#now = datetime(year = now.year, month = now.month, day = now.day)
#diff = now-dt
#datetime.timedelta(7)
#print diff.days
print "It looks like you were born on %s" %birthday


