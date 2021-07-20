import sys
number = sys.argv[1]
number = int(number)
list_factors = []
for element in range(1, number+1):
    if number % element == 0:
        list_factors.append(element)

print (list_factors)





