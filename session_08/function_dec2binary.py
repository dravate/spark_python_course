import sys
def decToBin(n):
	if n == 0:
		return '0'
	else:
		return decToBin(int(n/2)) + str(n % 2)
'''
d = decToBin(int(sys.argv[1]))
print (d)
'''



