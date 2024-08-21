# solutions below are based in part on:
# wget http://jarrodmillman.com/capstone/code/senators.py
# wget http://jarrodmillman.com/capstone/code/senators2.py

import json
import string
from operator import itemgetter
import re
import numpy as np
import pandas as pd

# 1. Load the *senators-list.json* and *timelines.json* files as objects called *senators* and *timelines*.

# using 'with' here closes the file automatically
import os
os.chdir('project')  # if needed 

with open("senators-list.json") as f:
    senators = json.load(f)

with open("timelines.json") as f:
    timelines = json.load(f)

# 2. What type of datastructure is *timelines*? How many timelines are there? What does each timeline correspond to?

type(timelines)
type(timelines[0])
type(timelines[0][0])

len(timelines)  # 100 senators
len(timelines[0]) # 200 tweets
timelines[0][0]

timelines[0][0].keys()
timelines[0][0]["text"]

timelines[0][0]["user"].keys()
timelines[0][0]["user"]['screen_name']
timelines[0][0]["user"]["followers_count"]

# 3. Make a list of the number of followers each senator has.

len(senators)
senators.keys()
len(senators['users'])
senators['users'][0].keys()

popularity = [(s['name'], s['followers_count']) for s in senators['users']]


# 4. What is the screen name of the senator with the largest number of followers.

popularity.sort()  # this will only work if you have 'followers_count' as the first element of the tuples in popularity

# this works as is, but is a bit advanced
popularity.sort(key = lambda x: x[1], reverse = True)

popularity[0]
popularity[0:10]

# alternatively, put the info in a pandas DataFrame

import pandas as pd
popularity = pd.DataFrame(popularity).rename(columns = {0:'name',1:'followers_count'})
popularity.sort_values('followers_count', ascending = False)

# 5. Make a list of lists where the outer list represents senators and the inner list contains each senator's tweets, and call it *tweets*.

# approach #1: list comprehension within a loop
tweets = []
for timeline in timelines:  # loop over senators
    tweets.append([tweet['text'] for tweet in timeline])  # list comprehension to loop over a senator's tweets

# approach #2: double list comprehension
tweets = [ [tweet['text'] for tweet in timeline] for timeline in timelines]

# approach #3: double for loop
tweets = []
for timeline in timelines:  # loop over senators
    tmp = []
    for tweet in timeline:
        tmp.append(tweet['text'])
    tweets.append(tmp)



