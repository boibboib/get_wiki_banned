import praw
import re
import sys

# copy c:\Python26\lib\site-packages\praw\praw.ini to %appdata%
# edit user and pswd

user_agent = ("boib_1.0 by /u/boib")
r=praw.Reddit(user_agent=user_agent)
r.login()
x = r.get_subreddit("books")
y = x.get_wiki_page("automoderator")

# # User shadowbans\r\n    user: [babyjames,

b = re.search('#\s*User shadowbans\s*user:\s*\[(.+)\]', y.content_md)           
bb = b.group(1)
f = bb.split(',')

# remove leading/trailing white space?
f = [x.lstrip() for x in f]
f = [x.rstrip() for x in f]

gone = []
for i in f:
    try:
        print "Getting user %s" % i
        v = r.get_redditor(i)

    except:
        #print "Unexpected error:", sys.exc_info()[0]
        print "========= user %s appears to be gone" % i
        gone.append(i)
        pass

print "\n-------------------------------\nList of gone!\n-------------------------------"
for i in gone:
    print i


