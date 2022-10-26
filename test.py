import praw
import pdb
import re
import os
import time
from datetime import datetime, timedelta

reddit = praw.Reddit(
  "bot1",
  config_interpolation="basic",
)

subreddit = reddit.subreddit("/vinylcollectors")

for submission in subreddit.new(limit=10):
  print(submission.title)
  print("---------------\n")
  print(submission.selftext + '\n' + '=\n')
