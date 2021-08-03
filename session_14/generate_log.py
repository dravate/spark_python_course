from optparse import OptionParser
from faker import Faker
from datetime import datetime, timedelta
import random


def generate_days_timestamp(day):
    '''
    for given datetime - return the random number of timestamps for the day
    '''
    random_entities = random.randint(0, 86400)
    return [day + timedelta(seconds=entry) for entry in range(random_entities) ]


def get_dateslist( start_date, end_date):
    number_days  = start_date - end_date
    return [start_date + timedelta(day) for day in range(number_days.days)]


def main():
    parser = OptionParser(
        usage="usage: %prog [options] filename",
        version="%prog 1.0"
    )
    parser.add_option(
        "-s", "--start",
        action="store_true",
        dest="start",
        default=False,
        help="The starting Date  - YYYY-MM-DD format")
    parser.add_option(
        "-e", "--end",
        action="store_true",
        dest="end",
        default=False,
        help="The Ending Date  - YYYY-MM-DD format")

    parser.add_option(
        "-c", "--count",
        action="store", # optional because action defaults to "store"
        dest="count",
        #default=100,
        help="Maximum Number of lines for each day",
    )
    (options, args) = parser.parse_args()

    #if len(args) != 1:
    #    parser.error("wrong number of arguments")
    print (options)
    print (args)
    days = get_dateslist(
        datetime.strptime(args[1], '%Y-%m-%d'),
        datetime.strptime(args[0], '%Y-%m-%d')
    )
    #print (days)
    log_lines = [generate_days_timestamp(d) for d in days]
    for entries in log_lines:
        for entry in entries:
            print (entry.strftime('%y-%m-%d %M-%H-%S  %z'))



if __name__ == '__main__':
    main()