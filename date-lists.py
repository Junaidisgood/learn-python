# import date module and assign as object date
# similar to java:
# Class objectName = new Class
import datetime as dt
# create list to store dates
dates = []
# add dates using append func
dates.append(dt.date(2020, 8, 22))
dates.append(dt.date(2003, 1, 18))
dates.append(dt.date(2020, 7, 22))
dates.append(dt.date(2020, 12, 27))
# sort in ascending order
dates.sort()
for date in dates:
    print(f"{date:%d/%m/%y}")
# sort in descending order
print("------descending---------")
dates.sort(reverse=True)
for date in dates:
    print(f"{date:%d/%m/%y}")