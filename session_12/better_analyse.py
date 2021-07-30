
if __name__ == '__main__':
    twiki_users = {}
    with open('TWiki_Application.log', 'r') as log:
        for line in  log.readlines():
            fields = line.split('|')
            fields = list(map(lambda x: x.strip(), fields))
            if fields[2] in twiki_users.keys():

                twiki_users[fields[2]] = twiki_users[fields[2]].append([fields[0], fields[1]])
            else:
                twiki_users[fields[2]] = [[fields[0], fields[1]]]

print (twiki_users)
