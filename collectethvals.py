# -*- coding: utf-8 -*-
import gdax
import datetime
import pandas as pd
import numpy as np
from datetime import datetime


# collect data from May 1, 2017 to Aug 9, 2017 as training
# 2017-05-01T00:00:00-04:00 = 1493611200
# 2017-08-09T00:00:00-04:00 = 1502251200
# 100 days or 2400 hours of data
# -> adjust more
# collect data from Aug 9, 2017 to Nov 17, 2017 as test data
# 2017-08-09T01:00:00-04:00 = 1502254800
# 2017-11-17T00:00:00-04:00 = 1510891200
# 100 days or 2400 hours of data
# -> adjust less

def collectOldVals(timeunit, starttime, endtime, file):
	public_client = gdax.PublicClient()
	datafile = open(file,'w') 

	# translate from Unix time stamp
	# can also do it one-by-one and manipulate each row
	start_unix = int(starttime)

	while(start_unix < endtime):
		end_unix = start_unix + (timeunit * 200)
		print end_unix
		
		# keep times in Eastern Time
		start_iso = datetime.fromtimestamp(start_unix).isoformat() +'-04:00'
		end_iso = datetime.fromtimestamp(end_unix).isoformat() +'-04:00'

		# store data temporarily as strings
		hist_rates = str(public_client.get_product_historic_rates('ETH-USD', start_iso, end_iso, granularity = timeunit))

		datafile.write(hist_rates)

		start_unix = end_unix

# training data
collectOldVals(3600, 1493611200, 1502251200, 'trainingdata.txt')
# test data
collectOldVals(3600, 1502254800, 1510891200, 'testdata.txt')


# need to convert data to usable dataframe

# collect most recent value 



