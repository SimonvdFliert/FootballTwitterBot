# https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f
# https://realpython.com/twitter-bot-python-tweepy/#the-fav-retweet-bot

import tweepy
import datetime

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# handles our login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# store the access request token
auth.set_access_token(access_token, access_token_secret)

# api stores the authorization settings
api = tweepy.API(auth)

def publictweet(): 
    if datetime.date.today().weekday() == 0:
        tweettopublish = "Test tweet"
    if datetime.date.today().weekday() == 1:
        tweettopublish = "Test tweet"
    if datetime.date.today().weekday() == 2:
        tweettopublish = "Test tweet"
    if datetime.date.today().weekday() == 3:
        tweettopublish = "Test tweet"
    if datetime.date.today().weekday() == 4:
        tweettopublish = "Test tweet"
    if datetime.date.today().weekday() == 5:
        tweettopublish = "Test tweet"
    if datetime.date.today().weekday() == 6:
        tweettopublish = "Test tweet"

    api.update_status(tweettopublish)
    print(tweettopublish)

publictweet()


