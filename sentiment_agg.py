# -*- coding: utf-8 -*-
import nltk
import gdax
import datetime
import pandas as pd
import numpy as np
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Analyze the aggregate sentiment values for a dataset
def listSentiVals():
	df_NN_pickle = pickle.load(open('NN_pickled_time.p', 'rb'))
	
	#create lists for averaging and counters to count respective number of pos/neg news
	neg = []
	neu = []
	pos = []
	comp = []
	negcount = 0
	poscount = 0

	for index, row in df_NN_pickle.iterrows():
		neg.append(row['neg'])
		neu.append(row['neu'])
		pos.append(row['pos'])
		comp.append(row['compound'])

		if (row['compound'] <= (-0.5)):
			negcount += 1
		elif (row['compound'] >= 0.5):
			poscount += 1
			
	neg_avg = sum(neg)/len(neg)
	pos_avg = sum(pos)/len(pos)
	neu_avg = sum(neu)/len(neu)
	comp_avg = sum(comp)/len(comp)

	print('Reddit Aggregate - neg: {}, neu: {}, pos: {}, comp: {}. #pos: {}, #neg: {}').format(neg_avg, neu_avg, pos_avg, comp_avg, poscount, negcount)

listSentiVals()
