import sys

a = int(sys.argv[1])
operation = sys.argv[2]
b = int(sys.argv[3])

print(operation)

def calculate(a, b, operation):
    if operation == '+':
        return a + b
    if operation == 'x':
        return  a*b

print (calculate(a, b, operation))