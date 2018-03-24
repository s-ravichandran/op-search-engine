import newBayes
import csv
import nltk
from newBayes import *
import pickle

f= open('data/my_classifier.pickle')
classifier = pickle.load(f)
f.close()
positive = []
negative = []
tf = open('data/tweets.txt','r')
line = tf.readline()
while line:
	outcome = classifier.most_likely_outcome(nltk.word_tokenize(line))
	if(outcome=='4'):
		positive.append(line)
	elif(outcome=='0'):
		negative.append(line)
	line = tf.readline()
tf.close()

print 'POS'
fpos = open('data/positive_tweets.txt','wb')
fpos.truncate()
for item in positive:
	fpos.write(item)
	# print item
fpos.close()

print 'NEG'
fneg = open('data/negative_tweets.txt','wb')
fneg.truncate()
for item in negative:
	fneg.write(item)
	# print item
fneg.close()

print '\n\n'	
overall = ''
pos_count = len(positive)
neg_count = len(negative)

if(pos_count > neg_count):
	overall = 'Overall Opinion is Positive'
elif(neg_count > pos_count):
	overall = 'Overall Opinion is Negative'
else:
	overall = 'Overall Opinion is Neutral'

print overall
