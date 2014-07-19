get_wiki_banned
===============

Reddit - verify users in a subreddit's automod shadowban list are not deleted or banned by admin in order to remove deleted accounts from the list.

Requirements:

1. PRAW library.
2. Must be a moderator, or have wiki read privileges.
3. This script assumes that the automoderator shadowban rule has this header:
     # User shadowbans

Usage:
1. Edit USERNAME, PASSWORD and SUBREDDIT vars in get-wiki-banned.py.
2. Run get-wiki-banned.py

The script will retrieve the shadowban list from reddit.com/r/SUBREDDIT/wiki/automoderator and attempt to access each username to asses if the account has been deleted or shadowbanned by admin.
When complete, the script will print out the usernames that have been deleted or shadowbanned by admin.

