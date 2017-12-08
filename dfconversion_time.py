# -*- coding: utf-8 -*-
import nltk
import unicodedata
import gdax
import datetime
import pandas as pd
import numpy as np
import pickle
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def storeValsinDF(textfile):
	listoflists = pickle.load(open('eth_price_pickle.p', 'rb'))
	# price data
	datetimes = [sublist[0] for sublist in listoflists]
	prices = [sublist[3] for sublist in listoflists]
	vols = [sublist[5] for sublist in listoflists]

	data = {'datetime': datetimes, 'prices': prices, 'volume': vols}
	df_price = pd.DataFrame(data)

	# reddit
	fp = open(textfile, 'r')
	df_reddit = pd.read_csv(fp, usecols=[3,6])
	df_reddit.sort_values('created_utc')

	# google news
	fp_news = open('news-ethereum5.csv','r')
	df_news = pd.read_csv(fp_news, usecols=[0,3,4])
	df_news['description'] = df_news['description'].apply(lambda x : str(x))

	# NN dataframe - save all in here
	df_NN = pd.DataFrame(index = range(0,(df_news.shape[0] + df_reddit.shape[0] - 1)), columns = ['prev_price', 'compound', 'neg', 'neu', 'pos', 'next_price', 'datetime'])

	sid = SentimentIntensityAnalyzer()
	
	df_price.sort_values('datetime')
	df_price.drop_duplicates(subset = 'datetime')

	for index, row in df_reddit.iterrows():
		ss = sid.polarity_scores(row['title'])
		df_NN.set_value(index,'compound', ss['compound'])
		df_NN.set_value(index, 'neg', ss['neg'])
		df_NN.set_value(index, 'neu', ss['neu'])
		df_NN.set_value(index, 'pos', ss['pos'])
		# time calc
		prev_time = row['created_utc'] - (row['created_utc'] % 3600)
		#print index

		row_price = df_price.loc[df_price['datetime'] == prev_time]

		if not row_price.empty:
			df_NN.set_value(index, 'prev_price', row_price.iloc[0,1])
			df_NN.set_value(index, 'next_price', float(df_price.loc[[row_price.index[0] + 1]]['prices']))
			df_NN.set_value(index, 'datetime', prev_time)
	
	for index, row in df_news.iterrows():
		ss_d = sid.polarity_scores(row['description'])
		ss_t = sid.polarity_scores(row['title'])
		df_NN.set_value(index + (df_reddit.shape[0]),'compound', ((ss_t['compound']+ss_d['compound'])/2))
		df_NN.set_value(index + (df_reddit.shape[0]), 'neg', ((ss_t['neg']+ss_d['neg'])/2))
		df_NN.set_value(index + (df_reddit.shape[0]), 'neu', ((ss_t['neu']+ss_d['neu'])/2))
		df_NN.set_value(index + (df_reddit.shape[0]), 'pos', ((ss_t['pos']+ss_d['pos'])/2))
		# time calc
		prev_time = row['publishedAt'] - (row['publishedAt'] % 3600)

		#print index + (df_reddit.shape[0])
		row_price = df_price.loc[df_price['datetime'] == prev_time]

		if not row_price.empty:
			df_NN.set_value(index + (df_reddit.shape[0]), 'prev_price', row_price.iloc[0,1])
			df_NN.set_value(index + (df_reddit.shape[0]), 'next_price', float(df_price.loc[[row_price.index[0] + 1]]['prices']))
			df_NN.set_value(index + (df_reddit.shape[0]), 'datetime', prev_time)

	
	with open('NN_pickled_time.p', 'wb') as fp:
 		pickle.dump(df_NN, fp)

	print df_NN

def checkpickle():
	df_NN_pickle = pickle.load(open('NN_pickled_time.p', 'rb'))
	print df_NN_pickle

storeValsinDF('reddit-ethereum.csv')
# checkpickle()









