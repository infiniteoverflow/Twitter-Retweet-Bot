import tweepy
from time import sleep
from twitter_credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q=('#EXPLOREMLBLR -filter:retweets'), lang='en').items(5):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
