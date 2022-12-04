import tweepy, re, os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), 'twitter.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


__auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(__auth)


class TwitterFunctions:
    
    @staticmethod
    def getTweet(query : str) -> str:
        '''Searches for Tweets with the given query and returns one randomly'''
        if query == '':
            return ''
        tweets = api.search_tweets(q=query, count=100)
        tweet = TwitterFunctions.clean_tweet(tweets[0].text)
        return tweet

    # stolen from previous code ;)
    @staticmethod
    def clean_tweet(tweet : str):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        if tweet.startswith("RT @") :
            tweet = tweet.replace("RT ", "")
        tweet = re.sub("@[A-Za-z0-9_]+","", tweet)
        tweet = re.sub("#[A-Za-z0-9_]+","", tweet)
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())