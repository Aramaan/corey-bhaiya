import datetime

d = datetime.date(2001,10,24)
tday = datetime.date.today()
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())
tdelta = datetime.timedelta(weeks = 2)
print(tday - tdelta )
#date - date = timedelta
#date +- timedelta = date
print(tday-d)
print((tday-d).days)
print((tday-d).total_seconds())

t = datetime.time()