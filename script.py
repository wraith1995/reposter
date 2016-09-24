#!/usr/bin/env python3.4
import info
import praw

R = praw.Reddit("Subreddit poster")
R.login(username=info.user,password=info.password)
SAVED_LINKS = R.user.get_saved(limit=30)
SUBREDDIT_LINKS = R.get_subreddit(info.subreddit).get_new(limit=30)


SAVED_LINKS_TUPLES = map(lambda x: (x.title,x.url),list(SAVED_LINKS))
SUBREDDIT_LINKS_TUPLES =  map(lambda x: (x.title,x.url),list(SUBREDDIT_LINKS))

for (title,url) in SAVED_LINKS_TUPLES:
    if (title,url) not in SUBREDDIT_LINKS_TUPLES:
        print("Submitting {0} at {1}".format(title,url))
        R.submit(info.subreddit,title,url=url)



