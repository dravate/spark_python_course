class student:
	name=''
	age=0
	def __init__(self, name, age):
		self.name = name
		self.age = age

s1 = student('Bill', 25)
s2 = student('Steve', 29)
s3 = student('Ravi', 26)

student_list = [s1, s2, s3]
# student_list.sort() # raise an error

student_list.sort(key=lambda s: s.name) # sorts using lambda function

print('Students in Ascending Order:', end=' ')

for std in student_list:
	print(std.name, end=', ')

student_list.sort(key=lambda s: s.name, reverse=True) # sorts using lambda function

print('Students in Descending Order:', end=' ')

for std in student_list:
	print(std.name, end=', ')
