from textblob import TextBlob
from nltk.corpus import stopwords
import sys
from twython import Twython
import re
from pprint import pprint
import json

num_tweets = 100

# Parameters for OAuth

client_args = {
    'verify': False
}

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

query = sys.argv[1:]

def processTweet(tweet):
	tweet = tweet.lower()
	#Remove www.* or https?://*
	tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',tweet)
	#Remove @username
	tweet = re.sub('@[^\s]+','',tweet)
	#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
	#Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	#trim
	tweet = tweet.strip('\'"')
	return tweet

def getData(query):
	twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, client_args=client_args)
	search_results = twitter.search(q=query, rpp="50", count=num_tweets, lang='en')
	f = open('data/tweets.txt','wb')
	f.truncate()
	for tweet in search_results['statuses']:
		# tweet_text = processTweet(tweet['text'])
		tweet_text = tweet['text']
		f.write(tweet_text.encode('utf-8')+'\n')

if __name__ == "__main__":
	getData(query)
