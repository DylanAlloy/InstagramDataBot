import urllib2
import datetime
import time
import os

def proc(interval,username):
    while True:
        print "Finished first export. Sleeping for " + interval + " seconds.\n"
        try:
            file(os.path.dirname(os.path.realpath(__file__)) + "instagram.txt", "w").write(urllib2.urlopen("http://www.instagram.com/" + username).read())
            followers = str("followed_by\":{\"count\":")
            search = open(os.path.dirname(os.path.realpath(__file__)) + "instagram.txt","r")
            for line in search.readlines():
                if followers in line:
                    print line
                    print line.index(followers)
                    follows = line[line.index(followers) + 22],line[line.index(followers) + 23],line[line.index(followers) + 24],line[line.index(followers) + 25],line[line.index(followers) + 26]
                    number = ''.join(str(x) for x in follows)
                    documentprint = str((number, ":", datetime.datetime.now(),))
                    chars_to_remove = ['(','\'',',','datetime.datetime',')']
                    documentprint = documentprint.translate(None, ''.join(chars_to_remove))
                    with open(os.path.dirname(os.path.realpath(__file__)) + "followers.txt", "a") as f:
                        f.write(documentprint + '\n')
                        time.sleep(int(interval))
        except urllib2.HTTPError:
                time.sleep(2000)
                return()
def prompt():
    username = raw_input("What is your instagram username?\n")
    if len(username) < 1:
        print "Not a valid username."
    else:
        file(os.path.dirname(os.path.realpath(__file__)) + "followers.txt", "w")
        interval = raw_input("How often would you like to record(in seconds)?\n")
        if int(interval) < 60:
            opt = raw_input("That is very fast. You may experience decreased bandwidth on your network, continue? [Y/N]:\n")
            if opt == ("Y" or "y"):
                proc(interval,username)
            else:
                return()
        else:
            proc(interval,username)
prompt()
