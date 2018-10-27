from push_whatsapp import *


import json
import pandas as pd


tweets_data_path = './twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
		
		


tweet_text = []

for i in range(len(tweets_data)):
    try:
        string = tweets_data[i]['text']
        tweet_text.append(string)
    except:
        continue
		

for i in range(len(tweet_text)):
	push_whatsapp(tweet_text[i])