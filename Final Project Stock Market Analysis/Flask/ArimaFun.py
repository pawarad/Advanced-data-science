


from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

import matplotlib
import matplotlib.pylab as plt
#import matplotlib.finance as mpf
from flask import Flask, request, render_template
from matplotlib.pylab import rcParams
from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, iplot, iplot_mpl
#import statsmodels.api as sm
import warnings
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA

def Stock_name(cmpyname):
    from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
    params = [{'q':cmpyname}]
    period = "5Y"
    # get open, high, low, close, volume data (return pandas dataframe)
    df = get_prices_data(params, period)
    df.reset_index(level=None,inplace=True)
    df=df.rename(index=str, columns={"index": "Date"})
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df['Close_diff'] = df[cmpyname+'_Close']-df.shift()[cmpyname+'_Close']
    df['Close_diff_log'] = np.log1p(df[cmpyname+'_Close'])-np.log1p(df.shift()[cmpyname+'_Close'])
    df = df[[cmpyname+'_Close', 'Close_diff', 'Close_diff_log']]
    df = df.dropna()
    train=df[0:880] 
    test=df[880:]
    len(train), len(test)
    ts = train[cmpyname+'_Close'].as_matrix()
    predictions = np.empty((0), dtype=np.float32)
    for i in range(len(test)):
        arima_3_1_0 = ARIMA(ts, order=(3, 1, 0)).fit(dist=False)
        predict = arima_3_1_0.forecast()[0]
        predictions = np.hstack([predictions, predict])
        ts = np.hstack([ts, predict])
        predictions
        nans = np.zeros(len(train))
    nans[:] = np.nan
    orgs = pd.concat([train[cmpyname+'_Close'], test[cmpyname+'_Close']])
    orgs = pd.DataFrame({'Date': orgs.index,
                         'Original': orgs.as_matrix(),
                         'Prediction': np.hstack([nans, predictions])})
    orgs = orgs.set_index('Date')
    orgs.plot(color=['blue', 'red'])
    
    ## 1 year
    train=df[734:1100] 
    test=df[1100:]
    #return len(train), len(test)
    ts = train[cmpyname+'_Close'].as_matrix()
    predictions = np.empty((0), dtype=np.float32)
    for i in range(len(test)):
        arima_3_1_0 = ARIMA(ts, order=(3, 1, 0)).fit(dist=False)
        predict = arima_3_1_0.forecast()[0]
        predictions = np.hstack([predictions, predict])
        ts = np.hstack([ts, predict])
        nans = np.zeros(len(train))
    nans[:] = np.nan
    orgs = pd.concat([train[cmpyname+'_Close'], test[cmpyname+'_Close']])
    orgs = pd.DataFrame({'Date': orgs.index,
                         'Original': orgs.as_matrix(),
                         'Prediction(trend)': np.hstack([nans, predictions])})
    orgs = orgs.set_index('Date')
    orgs.plot(color=['blue'])
#     return (plt.show())
    plt.savefig('static/images/firstimage.png')
    return render_template("PredictionPage.html" , imagename="static/images/firstimage.png")
#     to call the created file that is made.
#     return('firstimage.png')








