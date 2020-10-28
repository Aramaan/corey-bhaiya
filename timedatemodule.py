import datetime
import pytz

# t = datetime.time(8 , 43 , 31, 200000)
t = datetime.datetime(2020, 10, 20, 8, 58, 23, 12345)
print(t)
print(t.date())
print(t.time())
print(t.hour)
tdel = datetime.timedelta(days=12, hours=15)
print(t + tdel)
print(datetime.datetime.today())
print(datetime.datetime.now())#it has time zone argument
print(datetime.datetime.utcnow())
dt = datetime.datetime(2020,10,24,22,10,15,12345, tzinfo=pytz.UTC)
dt_tdy = datetime.datetime.now(tz = pytz.UTC)
dt_tday = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
dt_mytz = dt_tdy.astimezone(pytz.timezone('US/Mountain'))
print(dt_tdy)
print(dt_mytz)
print(dt_tday)
print(dt)
# for tz in pytz.all_timezones:
#     print(tz)
# you cannot apply astimezone to a naive datetime
dt_mtn = datetime.datetime.now()
mnt_tz = pytz.timezone('US/Mountain')
dt_mtn = mnt_tz.localize(dt_mtn)
print(dt_tdy.isoformat())
print(dt_tdy.strftime('%B %d, %Y'))
dtt = 'October 21, 2020'
dtt_ = datetime.datetime.strptime(dtt , '%B %d, %Y')