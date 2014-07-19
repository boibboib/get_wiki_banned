import praw
import re
import sys



USERNAME = "xxxx"
PASSWORD = "xxxx"
SUBREDDIT = "xxxx"

user_agent = ("get-wiki-banned 1.0 by /u/boib")
r=praw.Reddit(user_agent=user_agent)

Trying = True
while Trying:
	try:
		r.login(USERNAME, PASSWORD)
		print('Successfully logged in\n')
		Trying = False
	except praw.errors.InvalidUserPass:
		print('Wrong Username or Password')
		quit()
	except Exception as e:
		print("%s" % e)
		time.sleep(5)


x = r.get_subreddit(SUBREDDIT)
y = x.get_wiki_page("automoderator")

# # User shadowbans\r\n user: [babyjames,

b = re.search('#\s*User shadowbans\s*user:\s*\[(.+)\]', y.content_md)
bb = b.group(1)
f = bb.split(',')

# remove leading/trailing white space
f = [x.lstrip() for x in f]
f = [x.rstrip() for x in f]

gone = []
for i in f:
    try:
        print ("Getting user %s" % i)
        v = r.get_redditor(i)

    except:
        #print "Unexpected error:", sys.exc_info()[0]
        print ("========= user %s appears to be gone" % i)
        gone.append(i)
        pass

print ("\n-------------------------------\nList of gone!\n-------------------------------")
for i in gone:
    print (i)


