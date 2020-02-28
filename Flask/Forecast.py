
# coding: utf-8

# In[5]:


import matplotlib
import matplotlib.pylab as plt
matplotlib.style.use('seaborn')
from matplotlib.pylab import rcParams
from plotly.graph_objs import *
# import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation
from matplotlib import style
import datetime
import math
from datetime import date
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from flask import Flask, request, render_template
import timestamp



# In[14]:


def Stock_name(cmpyname):
    from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
    params = [{'q':cmpyname}]
    period = "5Y"
    df = get_prices_data(params, period)
    forecast_col = cmpyname+'_Close'
    df.fillna(-99999,inplace=True)
    forecast_out = int(math.ceil(0.09*len(df)))
    df['label']=df[forecast_col].shift(-forecast_out)
    X = np.array(df.drop([cmpyname+'_Close'],1))
    X = X[:-forecast_out]
    X_lately = X[-forecast_out:]
    df.dropna(inplace=True)
    Y = np.array(df['label'])
    clf = LinearRegression(n_jobs=-1)
    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)
    clf.fit(X_train, Y_train)
    accuracy = clf.score(X_test, Y_test)
    style.use('ggplot')
    forecast_set = clf.predict(X_lately)
    df['Forecast'] = np.nan
    d = df.iloc[-1].name
    last_date=datetime.combine(d, datetime.min.time())
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day
    for i in forecast_set:
        next_date = datetime.fromtimestamp(next_unix)
        next_unix += 86400
        df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
    df.reset_index(level=None,inplace=True)
    df=df.rename(index=str, columns={"index": "Date"})
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    plt.figure(figsize=(20,8))
    df[cmpyname+'_Close'].plot()
    df['Forecast'].plot()
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')
    df['Forecast'].plot()
    df.reset_index(level=None,inplace=True)
    df=df[1050:]
    #print("inside")
    #var2 = "new"+str(timestamp)+".png"
    plt.savefig('static/images/var4')
    return(df)
    
    #plt.savefig('var1')
    # return(plt.show())

    


# In[15]:


# Stock_name('FB',3)

