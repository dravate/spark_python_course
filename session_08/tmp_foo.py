def foo():
    try:
        print("I am line inside try")
        print("I am actually another line")
        x = 5 * 5
        return 1
    finally:
        print ("Hello")
        print (x)


print(foo())
