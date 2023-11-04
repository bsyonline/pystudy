import time

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print(datetime.datetime.now())
new_date = datetime.timedelta(days=10)
print(datetime.datetime.now() + new_date)
day = datetime.datetime(2020,10,10)
print(day + datetime.timedelta(minutes=10))
