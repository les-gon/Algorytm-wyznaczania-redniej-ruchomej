import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import quandl
start = datetime.datetime(2018,5,1)
end = datetime.datetime(2019,1,1)
df = quandl.get('WSE/PKNORLEN', start_date=start, end_date=end)
window = 21
no_of_std = 2
rolling_mean = df['Close'].rolling(window).mean()
rolling_std = df['Close'].rolling(window).std()
df['Rolling Mean'] = rolling_mean
df['Bollinger High'] = rolling_mean + (rolling_std * no_of_std)
df['Bollinger Low'] = rolling_mean - (rolling_std * no_of_std)
df[['Close','Bollinger High','Bollinger Low']].plot()
