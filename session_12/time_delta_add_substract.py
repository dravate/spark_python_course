from datetime import datetime, timedelta
start = datetime(2021, 4, 1)
print (start)

new_s = start + timedelta (7)
print (new_s)
print (2*timedelta(12))
prev_s = start - 2 * timedelta(12)

print (prev_s)
