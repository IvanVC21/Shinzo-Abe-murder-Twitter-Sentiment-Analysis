# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:46:16 2022

@author: dilato
"""

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "shinzo abe lang:en until:2022-07-09 since:2022-07-08"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('shinzoabe_tweets.csv')