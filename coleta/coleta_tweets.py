import tweepy
import csv
consumer_key = "Digite sua key"
consumer_secret = "Digite seu secret"

access_token = "Digite seu token"
access_token_secret = "digite seu token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

arquvio = open('TWEETS_COM_LOCALIDADE_07_10_2018.csv', mode='a', encoding='utf-8')


def start():
    try:
        tweets = []
        for tweet in tweepy.Cursor(api.search, q='bolsonaro OR haddad', tweet_mode="extended", lang="pt-br",
                                   sice='2018-10-06', until='2018-10-08').items():
            write = csv.writer(arquvio, delimiter='|')

            if 'retweeted_status' in dir(tweet):
                tweet.full_text = tweet.retweeted_status.full_text
            else:
                tweet.full_text = tweet.full_text
            # print(tweet.full_text)

            write.writerow([tweet.id, tweet.created_at, tweet.user.screen_name, tweet.full_text, tweet.user.location])

            print(tweet.created_at, tweet.full_text)
            tweets.append(tweet)
        arquvio.close()

    except tweepy.error.TweepError as et:
        print(et)
    except Exception as e:
        print(e)