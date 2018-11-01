import matplotlib.pyplot as plt
import fix_yahoo_finance as yf  
data = yf.download('AAPL','2016-01-01','2018-01-01')
stockData1 = open("stockData1.txt","w")
stockData1.write(str(data))
stockData1.close()
data.Close.plot()
plt.show()