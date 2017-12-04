# -*- coding: utf-8 -*-
import nltk
import gdax
import datetime
import pandas as pd
import numpy as np
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')
# NLTK test: I haven't looked at the twitter stuff closely yet
# make a list of 10 sentences
# for each row, get the compound, neg, neu, pos scores and store in corresponding array

infile = open('sentimenttest_data.csv', 'r')
sid = SentimentIntensityAnalyzer()

for row in infile:
	ss = sid.polarity_scores(row)
	print("{:-<65} {}".format(row, str(ss)))
	#print ss['neg'] ---- for pulling out each corresponding score