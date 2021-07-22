import sys

random_list = ['a', 0, 2]
for entry in random_list:
    try:
        print("The entry value is: ", entry)
        r = 1 / int(entry)
        break
    except:
        print("Ooops!", sys.exc_info()[0], " occured")
        print("Next Entry")
        print("")

print("The reciprocal of {} is {}".format(entry, r))
