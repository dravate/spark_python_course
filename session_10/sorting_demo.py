import sys
class student:
	name=''
	age=0
	def __init__(self, name, age, std):
		self.name = name
		self.age = age
		self.std = std
	def __str__(self):
		return "(" + self.name + ", " + str(self.age) + ")==> Class: " + str(self.std)

s1 = student('Bill', 25, 9)
s2 = student('Steve', 29, 10)
s3 = student('Ravi', 26, 7)

student_list = [s1, s2, s3]
for s in student_list:
	print(s);

#sys.exit(0)


# student_list.sort() # raise an error

student_list.sort(key=lambda s: s.std) # sorts using lambda function
print('Students in Ascending Order:')

for std in student_list:
	print(std)

sys.exit(0)

student_list.sort(key=lambda s: s.name, reverse=True) # sorts using lambda function

print('Students in Descending Order:')
for std in student_list:
	print(std)
