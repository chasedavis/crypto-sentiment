# Twitter module for collecting tweets in realtime. Can get 50K tweets a day. Chase Davis.

import tweepy
import pandas as pd
import numpy as np
import json

# Twitter API Access Keys
from credentials import *

# API setup modified from https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'

    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def status_to_JSON(tweet):

    wanted_attr = ['created_at', 'id', 'text', 'source', 'user', 'is_quote_status', 'quote_count', 'reply_count', 'retweet_count', 'favorite_count', 'entities', 'lang']
    unwanted_attr = ['_json', 'author', 'entities', 'contributors', 'coordinates', 'favorited', 'filter_level', 'geo', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str',
'place', 'retweeted', 'source_url', 'timestamp_ms', 'truncated']
    for attr in unwanted_attr:
        delattr(tweet, attr)

    return str(tweet)
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        with open("textdata/ether_data.txt", "a") as myfile:
            myfile.write('\n' + status_to_JSON(status))
        return True

    def on_error(self, status):
        print status


api = twitter_setup()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['ether', 'ethereum'])
