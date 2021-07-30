import sys
import os

class Useractivity:
    username=''
    activity=[]
    def __init__(self, username, activity):
        self.username = username
        self.activity = activity
    def activity_count(self):
        return len(self.activity)
    def __str__(self):
        return self.username


def get_count(e):
    '''
    helps with sorting
    :param e:
    :return count:
    '''
    return e.activity_count()

def get_lines_list (log_file):
    '''
    Helps read the log file and return the list
    :param log_file:
    :return: list with log lines as elements
    '''
    log_lines = []
    with open (log_file, 'r')  as mylog:
        for line in mylog.readlines():
            log_lines.append(line)

    return log_lines

def get_fields( line ):
    '''
    :param line:
    :return list of attributes from line
     line = '| 2017-01-01 - 07:54:57 | BenazirBhutto | edit | Fullgc.WebHome |  | 171.155.32.163 | '
    '''
    line_fields = line.split('|') # The fields has space charactors
    line_fields  = map(lambda element: element.strip(), line_fields)
    return list(line_fields) # convert hat to list

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
    '''
    Log Lines Look as below: 
    
      | 2017-01-01 - 07:01:43 | JawaharlalNehru | view | Main.WebHome | Mozilla | 253.111.182.73 | 
      | 2017-01-01 - 07:01:48 | AlbertEinstein | view | Main.WebHome | Mozilla | 201.36.26.7 | 
       timestamp| UserName| Activity| Web.Topicname | Client |IP Address
   
    Typical Questions: 
    1. Print activity of particular user
    2. Get the list of unique users 
    3. Find Top 5 Active users 
    4. Find Most Busy Day
    5. Which IP was used most? 
    6. Which Topic is Most Read (view) 
    7. Which Topic was created most collaborative way? 
    '''

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

    # I have read the log file, has lines in list

    #for line in log_lines[0:4]:
    #    line_fields =  get_fields(line)
    #    #print (line_fields)


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
    '''
    unique_users - dictionary 
          key & values
          username [ 
                   [activity 1],
                   [activey 2]
                   .
                   .
          ]
          
    '''
    user_classes = []
    for user, activity in unique_users.items():
        tmp_userinstance = Useractivity(user, activity)
        user_classes.append(tmp_userinstance)
    print (user_classes[0].activity_count())
    user_classes.sort(key=get_count)
    print (user_classes[-1].activity_count())
    active_u = user_classes[-5:]
    for e in active_u:
        print (e, e.activity_count())

    sys.exit(0);
    user_and_count = []  # [[usernanme, count], ...]
    for tmp_user in unique_users.keys():
        #print(tmp_user, len(unique_users[tmp_user]))
        user_and_count.append([tmp_user, len(unique_users[tmp_user])])
    max =0
    active_user = []
    for element in user_and_count:
         #print(element)
         #print(max)
         #print(active_user)
         if max > element[1]:
             #max = element[1]
             #active_user = element
             pass
         else:
            max = element[1]
            active_user = element
         #s = input()

    print (active_user)

    sys.exit(0);

    print("\n")
    #for key in unique_users:
    #    print (key, unique_users[key][0:4])
    #
    #print ("Activity of User: ", user)
    #count = 0;
    #for activity in unique_users[user]:
    #    print (activity)
    #    count +=1
    #print ("{} user has done {} many activities".format(user, count ))
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
