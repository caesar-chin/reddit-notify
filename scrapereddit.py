import praw
import pdb
import re
import os
import time
from datetime import datetime, timedelta


def ScrapeReddit(sub, keywords):
  try:
    posts=[]
    reddit = praw.Reddit(
      "bot1",
      config_interpolation="basic",
    )

    subreddit = reddit.subreddit(sub)

    for submission in subreddit.new(limit=10):
      for keyword in keywords:
        if submission.title.lower().find(keyword) != -1:
          posts.append(submission)
          print("Match for " + keyword + ": " + submission.title)
          break
    time.sleep(2)

  except Exception:
    time.sleep(10)

  return posts
