import tweepy
import time

consumer_key = 'QWsvG3JxGUQRtSHWmUXc2jMpY'
consumer_secret = 'HEgF2toVbkS8gduVI26Y98VMN1TiwPxx0Jx2ZI3zAp5apsUq9w'

key = '767967551305297920-NBKUDZAKMZoNXD8qTd2biG5LeWoL5pI'
secret = 'csQ4J8heCG37EzOL5hW1yW8GrkMXHPp9pkdc5mygsvikz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
#api = tweepy.API(auth, wait_on_rate_limit=True)
api = tweepy.API(auth)
FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied to ID -" + str(tweet.id))
            api.update_status('@' + tweet.user.screen_name + "Good Job!!!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
while True:
    reply()
    time.sleep(15)
