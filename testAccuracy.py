import newBayes
import csv
import nltk
from newBayes import *
import pickle

f= open('data/my_classifier.pickle')
classifier = pickle.load(f)
f.close()

correct_count=0
wrong_count=0
line_count=0

with open('data/testing_set.csv','rb') as f:
	reader = csv.reader(f)
	for line in reader:
		outcome = classifier.most_likely_outcome(nltk.word_tokenize(line[1]))
		if(outcome == line[0]):
			correct_count+=1
		else:
			wrong_count+=1
		line_count+=1
		if(line_count>=100):
			print line_count
			line_count=0
print 'num_correct_tweets'
print correct_count
print 'num_wrong_tweets'
print wrong_count

total = correct_count+wrong_count
acc = float(correct_count)/total
print 'Efficiency = '
print acc
# print classifier.classify_tokens(nltk.word_tokenize(tweet))
