import tweepy, re, json

with open("../twitter/twitter.json","r") as file:
    keys = json.load(file)

__auth = tweepy.OAuth1UserHandler(
    keys.get('api_key'), keys.get('api_secret'), keys.get('access_token'), keys.get('access_token_secret')
)
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