import re

line = 'The   fox jumped   over    the        log'
pattern = re.compile('\s+')

line = re.sub(pattern, ' ', line)
print (line)

