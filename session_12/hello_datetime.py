from datetime import datetime
import sys
now = datetime.now()

print('The dateformat: {}'.format(now))
print ('The year is = {}'.format(now.year))
print ('The month is = {}'.format(now.month))
print ('The day is = {} '.format(now.day))


# datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) 
#
#                      Y  M  d   h  m    s      ms 
that_day = datetime(2021, 7, 1, 17, 9,  21, 832092)
print('The dateformat: {}'.format(that_day))
print ('The year is = {}'.format(that_day.year))
print ('The month is = {}'.format( that_day.month))
print ('The day is = {} '.format(that_day.day))

