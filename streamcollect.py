import tweepy
import pandas as pd
import numpy as np

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

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status
        return True

    def on_error(self, status):
        print status


api = twitter_setup()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['ether', 'ethereum'])


# if __name__ == '__main__':
#
#     #This handles Twitter authetification and the connection to Twitter Streaming API
#     l = MyStreamListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     stream = Stream(auth, l)
#
#     #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
#     stream.filter(track=['ether', 'ethereum'])
