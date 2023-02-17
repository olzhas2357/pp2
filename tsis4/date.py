# Write a Python program to subtract five days from the current date

from datetime import date, timedelta
today = date.today()
dt = date.today() - timedelta(5)
print(f'Today : {today}')
print(f'5 days after current Date : {dt}')

# Write a Python program to print yesterday, today, tomorrow

import datetime

x = datetime.datetime.now()
print("yesterday", x - datetime.timedelta(days = 1))
print("today", x)
print("tomorrow", x + datetime.timedelta(days = 1))


# Write a Python program to drop microseconds from datetime

import datetime

x = datetime.datetime.now()
print(x.strftime("%H"), x.strftime("%m"), x.strftime("%f"))


# Write a Python program to calculate two date difference in seconds

from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2023-02-17 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()


import datetime
















