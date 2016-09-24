#!/usr/bin/env python3.4
import info
import praw

R = praw.Reddit("Subreddit poster")
R.login(username=info.user,password=info.password)
SAVED_LINKS = R.user.get_saved(limit=30)



SAVED_LINKS_TUPLES = map(lambda x: (x.title,x.url),list(SAVED_LINKS))


for (title,url) in SAVED_LINKS_TUPLES:
    try:
        R.submit(info.subreddit,title,url=url)
        print("Submitting {0} at {1}".format(title,url))
    except praw.errors.AlreadySubmitted:
        pass


