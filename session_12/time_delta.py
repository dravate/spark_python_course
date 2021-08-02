from datetime import datetime
#           datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]) 
#                   Y  M   d   h   m  s      ms                
delta = datetime(2021, , 25, 18, 21, 1, 123000) \
         - datetime (2021, 1, 1, 18, 51, 51, 123000)
#                       Y  M  d   h   m  s      ms 
print(type(delta))
print(delta)
print (delta.days)
print (delta.seconds)



