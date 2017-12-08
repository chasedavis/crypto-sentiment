# -*- coding: utf-8 -*-
import gdax
import datetime
import pandas as pd
import numpy as np
from datetime import datetime


# collect etherum values using Unix time stamps
# toggle granualrity by changing the timeunity parameter

def collectOldVals(timeunit, starttime, endtime):
	public_client = gdax.PublicClient()
	listoflists = []

	start_unix = int(starttime)

	while(start_unix < endtime):
		# 200 datapoints max per candle group
		end_unix = start_unix + (timeunit * 200)
		
		# keep times in Eastern Time
		start_iso = datetime.fromtimestamp(start_unix).isoformat() +'-04:00'
		end_iso = datetime.fromtimestamp(end_unix).isoformat() +'-04:00'

		# store data temporarily as strings
		hist_rates = public_client.get_product_historic_rates('ETH-USD', start_iso, end_iso, granularity = timeunit)

		listoflists.append(hist_rates)
		
		start_unix = end_unix
	print listoflists

			# save info to pickle file 
	with open('eth_price_pickle.p', 'wb') as fp:
 		pickle.dump(listoflists, fp)

collectOldVals(3600, 1493611200, 1502251200)




