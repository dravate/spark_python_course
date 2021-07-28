import sys
import os

# Read the File


def get_lines_list (log_file):
    log_lines = []
    with open (log_file, 'r')  as mylog:
        for line in mylog.readlines():
            log_lines.append(line)

    return log_lines

def get_fields( line ):
    # line = '| 2017-01-01 - 07:54:57 | BenazirBhutto | edit | Fullgc.WebHome |  | 171.155.32.163 | '
    line_array = line.split('|')
    # Better ways, use regex, remove spaces
    #TODO - use map
    #new_array = []
    #for element in line_array:
    #    new_array.append(element.strip())
    new_array = map(lambda element: element.strip(), line_array)
    return list(new_array)

def create_dictionary_user_activity(user_activity_lines):
    #print (user_activity_lines)
    '''
    d  = {
    user = { activity_time:
             activity:
             topic:
             }


    :param user_activity_lines:
    :return:
    '''

    for line in user_activity_lines:
        print (line)

if __name__ == '__main__':
    #  python analyse_twiki_log.py TWiki_Application.log OprahWinfrey
    # execute this script as above line
    print(sys.argv)
    print (len(sys.argv))
    if len(sys.argv) != 3:
        print ("check your arguments")
        sys.exit(0)

    log_file = sys.argv[1]
    user = sys.argv[2]
    print("You have passed logfile: {}".format(log_file))
    # check the presence of the file
    if os.path.exists(log_file):
        print ("Reading Log File: ", log_file)
    else:
        print ("The {} is not present in filesystem".format(log_file))
        sys.exit(1)
    # At this stage - the log file is present


    log_lines = get_lines_list(log_file)
    #for element in log_lines[0:4]:
    #    print (element.strip())
    #sys.exit(0)

    # I have read the log file, has lines in list
    '''
    | 2017-01-01 - 07:01:43 | JawaharlalNehru | view | Main.WebHome | Mozilla | 253.111.182.73 | 
    | 2017-01-01 - 07:01:48 | AlbertEinstein | view | Main.WebHome | Mozilla | 201.36.26.7 | 
     timestamp| UserName| Activity| Web.Topicname | Client |IP Address
    TODO: print activity of particular user
    1. Get the list of unique users 
    2. Print Activity in-front of each user 
    3. How about finding most active User? 
    4. How about - which IP was used most? 
    5. How about finding busiest Day? 
    
    '''
    #for line in log_lines[0:4]:
    #    line_fields =  get_fields(line)
    #    #print (line_fields)
    #sys.exit(0)



    unique_users = {}
    for line in log_lines:
        line_fields = get_fields(line)
        #unique_users[line_fields[2]] = [line_fields[1]]
        if line_fields[2] in unique_users:
            unique_users[line_fields[2]].append([
                 line_fields[1],
                 line_fields[3],
                 line_fields[4],
                 line_fields[5]
                 ])
        else:
            unique_users[line_fields[2]] = [[
                line_fields[1],
                line_fields[3],
                line_fields[4],
                line_fields[5]
            ]]


    print("\n")
    #for key in unique_users:
    #    print (key, unique_users[key][0:4])
    #
    for activty in unique_users[user]:
        print (activty)
    sys.exit(0)

    # How many unique uers?
    #print (unique_users)
    #sys.exit(0)
    # Is BillGates Present in the log
    if 'BillGates' in unique_users:
        print ("Bill Gates is Present")
    else:
        print ("Bill Gates does not exists in the log file")
    sys.exit(0)
    user_activity_details = create_dictionary_user_activity(log_lines)
