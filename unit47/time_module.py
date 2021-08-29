import time
import datetime
from datetime import timedelta
print(time.time())
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(datetime.datetime.today())
d1 = datetime.datetime(2018, 5, 19)
print(d1)
d2 = datetime.datetime.strptime('2018-05-19', '%Y-%m-%d')
print(d2)
print(d1.strftime('%Y-%m-%d'))
print(d2.year, d2.month, d2.day, d2.hour, d2.minute, d2.second, d2.microsecond)
print(d1 - timedelta(days=20))
