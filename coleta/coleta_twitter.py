import json

from tweepy import StreamListener, OAuthHandler, Stream


class TwitterListener(StreamListener):
    def __init__(self):
        super().__init__()
        self.cont_tweet = 0
        self.max_tweets = 5000

    def on_data(self, data):
        tweet = json.loads(data)
        user = tweet.get('user')
        if user.get('lang') == 'pt':
            id = tweet.get('id')
            message = tweet.get('text')
            tokens = message.split()
            tw = ""
            for token in tokens:
                tw = tw + " " + token
            message = tw
            favorites = tweet.get('favorite_count')
            #salva_csv(id, message, favorites)
        if self.cont_tweet >= self.max_tweets:
            return False

def start(tags):
    access_token = "2679888692-HhCNqOwUFvBIdI1YuaHTD6VXUE2pgJpt6gBGhSG"
    access_token_secret = "Hzhup6TWl9NSqwLCw6JLW5uLtfUFMMunYwqReNImIkKhp"
    consumer_key = "MNpjEht4TZnp21x7cFFUibcu3"
    consumer_secret = "FHzS2dRLxHpPjkgUfQR0LeDBa0gqPH1mBpmlkv8KEBb5PyPZjK"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=tags)