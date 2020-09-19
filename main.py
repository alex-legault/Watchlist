from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from datetime import date
import json

#Use Alpha Vantage API Key to access updated stock market data and metadata
ts = TimeSeries(key='5ZRUIOQ3NN7GYT1Z')

#convert a ticker's daily information to json object
msft = ts.get_daily(symbol='MSFT')
msft_str_obj = json.dumps(msft)
msft_json_obj = json.loads(msft_str_obj)

#find latest date ticker was closed
#this implies the watchlist does not track intraday activity
latest_date = msft_json_obj[1]["3. Last Refreshed"]

print(type(msft_json_obj[0][latest_date]['4. close']))
print(msft_json_obj[0][latest_date]['4. close'])

#print(type(msft))
#print(type(formatted_msft))
#print(formatted_msft)