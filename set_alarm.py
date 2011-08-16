#!/usr/bin/python
# Script to automatically set wake up alarm for the next day. Set this as a cronjob

__author__ = "Rag Sagar.V"
__email__ = '@'.join(['ragsagar','.'.join([_ for _ in ['gmail','com']])])


from time import mktime, strptime
from datetime import date, timedelta

ALARM_TIME = "02:05:00"  # Time to wakeup

# Finding the next date
next_date = date.today() + timedelta(days=1)
# Setting wakeup time for the next day
wakeup_time = "%d-%d-%d %s" % ( next_date.year, next_date.month, next_date.day, ALARM_TIME)
time_pattern = "%Y-%m-%d %H:%M:%S"
# Converting it to epoch time
epoch_seconds = int(mktime(strptime(wakeup_time, time_pattern))) 
alarm_file = file("/sys/class/rtc/rtc0/wakealarm","w")
alarm_file.write(str(epoch_seconds))
alarm_file.close()



