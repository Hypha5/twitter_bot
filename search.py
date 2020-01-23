import tweepy
import time

consumer_key = 'QWsvG3JxGUQRtSHWmUXc2jMpY'
consumer_secret = 'HEgF2toVbkS8gduVI26Y98VMN1TiwPxx0Jx2ZI3zAp5apsUq9w'

key = '767967551305297920-NBKUDZAKMZoNXD8qTd2biG5LeWoL5pI'
secret = 'csQ4J8heCG37EzOL5hW1yW8GrkMXHPp9pkdc5mygsvikz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetnumber = 3
tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)
def search():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retwet done")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
search()
