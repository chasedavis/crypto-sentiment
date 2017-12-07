# -*- coding: utf-8 -*-
import nltk
import gdax
import datetime
import pandas as pd
import numpy as np
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#positive sentiment: compound score >= 0.5
#neutral sentiment: (compound score > -0.5) and (compound score < 0.5)
#negative sentiment: compound score <= -0.5

#nltk.download('vader_lexicon')

infile = open('sentimenttest_data.csv', 'r')
sid = SentimentIntensityAnalyzer()

neg = []
neu = []
pos = []
comp = []
negcount = 0
poscount = 0

for row in infile:
	ss = sid.polarity_scores(row)
	print ss
	neg.append(ss['neg'])
	neu.append(ss['neu'])
	pos.append(ss['pos'])
	comp.append(ss['compound'])
	
	if (ss['compound'] <= (-0.5)):
		negcount += 1
	elif (ss['compound'] >= 0.5):
		poscount += 1


neg_avg = sum(neg)/len(neg)
pos_avg = sum(pos)/len(pos)
neu_avg = sum(neu)/len(neu)
comp_avg = sum(comp)/len(comp)

print('Reddit Aggregate - neg: {}, neu: {}, pos: {}, comp: {}. #pos: {}, #neg: {}').format(neg_avg, neu_avg, pos_avg, comp_avg, poscount, negcount)