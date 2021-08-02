# TODO - analyse TWIki log according to days
# print days activity count
# Example:
#     2021-01-01:  105 topics viewed
#                  10  topics edit


import getopt
import sys


if __name__=='__main__':
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "d:",
                                   ["date=",])
    except:
        print("Error: I could not parse")
        sys.exit(1)

    requested_dates = []
    for opt, arg in opts:
        if opt in ['-d', '--date']:
            requested_dates.append(arg)

    print(requested_dates)




