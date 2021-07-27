import sys
import os
# Read the File

def get_lines_list (log_file):
    log_lines = []
    with open (log_file, 'r') as f:
        for line in f.readlines():
            log_lines.append(line)
    return log_lines

def get_username( line ):
    # line = '| 2017-01-01 - 07:54:57 | BenazirBhutto | edit | Fullgc.WebHome |  | 171.155.32.163 | '
    line_array = line.split(' | ')
    return line_array

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
    if len(sys.argv) < 2:
        print ("You need to provided logfile name as an argument")
        sys.exit(0)
    log_file = sys.argv[1]
    # check the presence of the file
    if os.path.exists(log_file):
        print ("Reading Log File: ", log_file)
    else:
        print ("The {} is not present in filesystem".format(log_file))
        sys.exit(0)
    # At this stage - the log file is present
    log_lines = get_lines_list(log_file)
    #print (log_lines)
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
    for line in log_lines:
        line_fields =  get_username(line)
        #print (line_fields[1])

    unique_users = {}
    for line in log_lines:
        line_fields = get_username(line)
        unique_users[line_fields[1]] = 1

    #print (unique_users)
    # How many unique users?
    print (len(unique_users))

    # Is BillGates Present in the log
    if 'BillGatesHari' in unique_users:
        print ("Bill Gates is Present")
    else:
        print ("Bill Gates does not exists in the log file")

    user_activity_details = create_dictionary_user_activity(log_lines)
