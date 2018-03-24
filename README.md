# Twitter Opinion Mining

I built an opinion search engine for Twitter. The following section describes the workflow. 

## Operation
 - The user provides a search query Q. 
 - I use the Twython API to extract tweets relevant to Q.
 - I run the pre-trained classifier on these tweets and produce results.
 - [Optional] The user may choose to provide feedback which will be used to retrain the classifier.

I implemented a Naive-Bayes classifier and trained it on a set of labeled tweets. This is then used to classify tweets in real-time as positive/negative in their intent.

## Files
 - [getTweets.py](https://github.com/s-ravichandran/twitter-opinion-mining/blob/master/getTweets.py): Extract tweets on a search topic using Twython
 - [newBayes.py](https://github.com/s-ravichandran/twitter-opinion-mining/blob/master/newBayes.py): My implementation of Naive-Bayes classification
 - [train.py](https://github.com/s-ravichandran/twitter-opinion-mining/blob/master/train.py): Train the classifier on labeled data
 - [classify.py](https://github.com/s-ravichandran/twitter-opinion-mining/blob/master/classify.py): Classify the stream of tweets as positive or negative
 - [testAccuracy.py](https://github.com/s-ravichandran/twitter-opinion-mining/blob/master/testAccuracy.py): Classifier evaluation

## Requirements
The following modules are required for this to work. These can be installed with pip.

- Textblob
- Twython
- NLTK
- Pickle

The keys are not updated. The training data is also not uploaded (due to size restrictions).
