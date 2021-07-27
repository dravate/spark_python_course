from datetime import datetime
d_stamp = datetime(2021, 3, 31)
print(d_stamp)
print (str(d_stamp))
print ("---------------------\n")

# Use of strftime  - datetime to string 
print (d_stamp.strftime('%Y/%m/%d   %h:%S'))
print (d_stamp.strftime('%Y-%m-%d'))
print (d_stamp.strftime('%Y, %d %m'))
print ("---------------------\n")

# Use of strptime - strings to datetime 
d = '2021-03-31'

print (datetime.strptime(d, '%Y-%m-%d'))
print ("---------------------\n")

datestrs = ['01/Jan/2021', '01/Feb/2021', '01/Mar/2021', '01/Apr/2021']
print ([datetime.strptime(x, '%d/%b/%Y') for x in datestrs])
print ("---------------------\n")

my_list = [datetime.strptime(x, '%d/%b/%Y') for x in datestrs]
for days in my_list:
    print(days) 
