
def fullname_method( ):
    title = 'Sir'
    fullname = lambda x, y: title + '  ' + x + ' ' + y
    return fullname

x = fullname_method()
z = x('Hari', 'Sadu')
print (z)

