# import datetime
# d=datetime.datetime.now()
# print(d)
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.hour)
# print(d.ctime())#current time
# print(d)

import calendar  # 캘린더 모듈 사용
import datetime  # date / time 에 대한 모듈

d = datetime.datetime.now()
print(calendar.month(d.year, d.month))
