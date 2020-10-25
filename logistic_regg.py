import numpy as np
import pandas as pd
import talib as ta
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import quandl 
import datetime
start = datetime.datetime(2005,10,20)
end = datetime.datetime(2019,1,1)
df = quandl.get('WSE/PGNIG', start_date=start, end_date=end)
df = df.dropna()
df = df.iloc[:,:4]
df.head()
df['SMA_100'] = df['Close'].rolling(window=100).mean()
df['Open-Close'] = df['Open'] - df['Close'].shift(1)
df['Open-Open'] = df['Open'] - df['Open'].shift(1)
df['RSI'] = ta.RSI(np.array(df['Close']), timeperiod =10)
df = df.dropna()
X = df.iloc[:,:9]
y = np.where(df['Close'].shift(-1) > df['Close'],1,-1)
split = int(0.7*len(df))
X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]
model = LogisticRegression()
model = model.fit (X_train,y_train)
pd.DataFrame(zip(X.columns, np.transpose(model.coef_)))
probability = model.predict_proba(X_test)
predicted = model.predict(X_test)
print(metrics.confusion_matrix(y_test, predicted))
print(model.score(X_test,y_test))
