name = "Hari Sadu"

def hellofunction(name=None):
    '''Hello Function Demonstration'''
    if name: 
        print ("Hello ", name, "!")
    else: 
        print ("Hello Function!")


print (hellofunction.__doc__)

