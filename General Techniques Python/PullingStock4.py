import matplotlib.pyplot as plt
import quandl
'''
data = quandl.get("WIKI/KO", start_date="2016-01-01", end_date="2018-01-01", api_key="Az1tgnMqJReS5YXSz7R8")
stockData1 = open("stockData1.txt","w")
stockData1.write("******")
stockData1.write(str(data))
stockData1.close()
data.Close.plot()
plt.show()
'''
#mydata = quandl.get("FRED/GDP")
#mydata = quandl.get("EIA/PET_RWTC_D", collapse="monthly")
data = quandl.get_table('ZACKS/FC', paginate=True)
print(data)

