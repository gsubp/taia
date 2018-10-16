import tweepy
import csv

import util

consumer_key = "Digite sua key"
consumer_secret = "Digite seu secret"

access_token = "Digite seu token"
access_token_secret = "digite seu token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def start():
    try:
        tweets = []
        for tweet in tweepy.Cursor(api.search, q='bolsonaro OR haddad', tweet_mode="extended", lang="pt-br",
                                   sice='2018-10-06', until='2018-10-08').items():
            if 'retweeted_status' in dir(tweet):
                tweet.full_text = tweet.retweeted_status.full_text
            else:
                tweet.full_text = tweet.full_text
            # print(tweet.full_text)
            util.salva_csv(tweet.user.id, tweet.id, tweet.full_text, tweet.created_at, tweet.favorite_count, tweet.location)
            print(tweet.created_at, tweet.full_text)
            tweets.append(tweet)

    except tweepy.error.TweepError as et:
        print(et)
    except Exception as e:
        print(e)