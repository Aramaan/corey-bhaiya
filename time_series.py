import pandas as pd
from datetime import datetime , timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.xkcd()

# dates =[
#         datetime(2020,10,18),
#         datetime(2020,10,19),
#         datetime(2020,10,20),
#         datetime(2020,10,21),
#         datetime(2020,10,22),
#         datetime(2020,10,23),
#         datetime(2020,10,24)
#         ]
#
# y = [9,1,6,5,0,3,7]

data = pd.read_csv('first.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace= True)
price_date = data['Date']
price_close = data['Close']
plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d %b, %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.show()