import tweepy
import csv

import util

consumer_key = "UDyQGLPZJAZLcpsvAgx0NfCh7"
consumer_secret = "EyJ4wznwMu0vY9TcuSnEHw9lExNWAPomT3B7jFO2VHMcGAuW9s"

access_token = "2813746711-kBaDm7ttZ051DY8TxZFYqtvompgb4q3ZN8ArEJL"
access_token_secret = "uVYoOyp4qDVcpdrZPfpdBb4po5r8ZEBS4lNgamNlk32d7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def start():
    try:
        tweets = []
        for tweet in tweepy.Cursor(api.search, q='bolsonaro OR haddad OR nordeste OR nodestino OR marina OR ciro', tweet_mode="extended", lang="pt-br",
                                   sice='2018-10-06', until='2018-10-08').items():
            if 'RT' not in tweet.full_text:
                if 'retweeted_status' in dir(tweet):
                    tweet.full_text = tweet.retweeted_status.full_text
                else:
                    tweet.full_text = tweet.full_text
                # print(tweet.full_text)
                util.salva_csv(tweet.user.id, tweet.id, util.tokens(tweet.full_text), tweet.created_at, tweet.user.location, tweet.user.name)
                print(tweet.created_at, tweet.full_text)
                tweets.append(tweet)

    except tweepy.error.TweepError as et:
        print(et)
    except Exception as e:
        print(e)