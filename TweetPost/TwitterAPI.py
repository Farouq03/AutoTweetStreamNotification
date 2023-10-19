import tweepy
from TwitchAPI import userCheck
import random

#Your Keys and Tokens
api_keys = "API KEYS"
api_secret = "API SECRET KEYS"
bearer_token = "BEARER TOKEN"
access_token = "ACCESS TOKEN"
access_token_secret = "SECRET ACCESS TOKEN"

client = tweepy.Client(bearer_token, api_keys, api_secret, access_token, access_token_secret) 

#Create Tweet 
while True:
    check = checkUser()
    if check == True:
        client.create_tweet(text= "ENTER YOUR TWEET HERE") 
        print("Tweet posted!")
        break

