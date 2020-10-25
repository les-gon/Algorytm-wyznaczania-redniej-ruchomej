import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl
import datetime
start = datetime.datetime(2018,1,1)
end = datetime.datetime(2019,1,1)
df = quandl.get('WSE/CDPROJECT', start_date=start, end_date=end)
df.head()
df_close = pd.DataFrame(df.Close)
df_close['MA_30'] = df_close.Close.rolling(30).mean()
plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(df_close['Close'],label='CDP')
plt.plot(df_close['MA_30'], label='MA 30 day')
plt.legend(loc=2)
plt.show()
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
