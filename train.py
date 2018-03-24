import newBayes
import csv
from newBayes import *
import nltk
import re
import pickle

def getStopWordList(stopWordListFileName):
	stopWords = []
	stopWords.append('AT_USER')
	stopWords.append('URL')
	fp = open(stopWordListFileName, 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords

def preprocess(tweet):
	tweet = tweet.lower()
	#Convert www.* or https?://* to URL
	tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
	#Convert @username to AT_USER
	tweet = re.sub('@[^\s]+','AT_USER',tweet)
	#Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	tweet = re.sub('@|!|\?|;|:|\.|\&|-','',tweet)
	tweet = re.sub('\'','',tweet)
	tweet = re.sub('[0-9]','',tweet)
	#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
	#trim
	tweet = tweet.strip('\'"')
	return tweet

stopwords = []
non_stop_tokens = []
stopwords = getStopWordList('data/stopwords.txt')
def train():
	classifier = newBayes.Classifier(["4", "0"])
	count=0
	with open('data/training_set.csv','rb') as f:
		reader = csv.reader(f)
		for line in reader:
			senti = line[0]
			text = preprocess(line[1])
			# print senti
			# print text
			tokens = nltk.word_tokenize(text)
			for word in tokens:
				non_stop_tokens = []
				if(word not in stopwords):
					non_stop_tokens.append(word)
			# print non_stop_tokens
			classifier.add_training_example(senti, non_stop_tokens)
			count+=1
			# print count
			if(count>=1000):
				print count
				break
		f.close()
	
	top_features = classifier.get_top_features()
	# print top_features
	for features in top_features.values():
		print features

if __name__ == "__main__":
	train()
