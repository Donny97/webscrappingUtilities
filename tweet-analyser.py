import tweepy
from textblob import TextBlob

consumer_key= 'VdIsuFmHoCUvZsHkvuAWC1Kdk'
consumer_secret= 'hvmdPcwGSAfVSAYX2cyicMbzTremolCybJLffnV6SWRzJQKVyc'

access_token='823916208281923588-ZrdGtuO3xStXQq2UoJfZ20FrbJlDmRk'
access_token_secret='fNZl8R4QTserqlrumZ7jPhNT1gvWaLmB3jVF1tFPud83G'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Enter your test word here')

for tweet in public_tweets:
    print(tweet.text)
    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")