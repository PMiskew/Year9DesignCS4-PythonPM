from pandas_datareader import data as pdr

import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data1 = pdr.get_data_yahoo("AAPL", start="2017-02-15", end="2017-04-30")
#print(data1)
stockData1 = open("stockData1.txt","w")
stockData1.write(str(data1))
# download Panel
#data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")