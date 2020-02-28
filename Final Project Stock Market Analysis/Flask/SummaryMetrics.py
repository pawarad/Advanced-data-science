
# coding: utf-8

# In[3]:

import matplotlib
import matplotlib.pylab as plt
# import matplotlib.finance as mpf
# matplotlib.style.use('seaborn')
# get_ipython().magic('matplotlib inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 5
from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, iplot, iplot_mpl
import statsmodels.api as sm
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from sklearn import preprocessing,cross_validation
from matplotlib import style
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
from datetime import date
from datetime import datetime


# In[4]:

def summary_metrics(compnyname):
    from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
    params = [{'q':compnyname}]
    period = "5Y"
    df = get_prices_data(params, period)
    Model_name = []
    Mean_squared_error = []
    R2_score = []
    model = LinearRegression
    clf = LinearRegression(n_jobs=-1)
    X = df.iloc[:,[0,1,2,4]].values
    Y = df.iloc[:,3].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=np.random)
    clf.fit(X_train,Y_train)
    filename1 = 'Linear_Regression_model.pckl'
    pickle.dump(clf,open(filename1,'wb'))
    prediction1=clf.predict(X_test)
    MSE = mean_squared_error(Y_test, prediction1)
    R2 = r2_score(Y_test,prediction1)
    Model_name.append(' LinearRegression')
    Mean_squared_error.append(MSE)
    R2_score.append(R2)
    model = RandomForestRegressor
    regressor = RandomForestRegressor()
    X = df.iloc[:,[0,1,2,4]].values
    Y = df.iloc[:,3].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=np.random)
    regressor.fit(X_train,Y_train)
    filename2 = 'Random_Forest_Regressor_model.pckl'
    pickle.dump(regressor,open(filename2,'wb'))
    prediction2=regressor.predict(X_test)
    MSE = mean_squared_error(Y_test, prediction2)
    R2 = r2_score(Y_test,prediction2)
    Model_name.append('RandomForestRegressor')
    Mean_squared_error.append(MSE)
    R2_score.append(R2)
    model = ARIMA
    df = get_prices_data(params, period)
    df.reset_index(level=0,inplace=True)
    df=df.rename(index=str, columns={"index": "Date"})
    df['Date'] = pd.to_datetime(df['Date'])
    df1= df.set_index('Date')
    df2=df1[compnyname+'_Close']
    model = ARIMA(df2, order=(3,1,0))
    model_fit = model.fit(disp=0)
    filename = 'ARIMA_model.pckl'
    pickle.dump(model,open(filename,'wb'))
    X = df2.values
    size = int(len(X) * 0.80)
    train = X[0:size]
    test = X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(5,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        ('predicted=%f, expected=%f' % (yhat, obs))
        
    MSE = mean_squared_error(test, predictions)
    R2 = r2_score(test,predictions)
    Model_name.append('ARIMA')
    Mean_squared_error.append(MSE)
    R2_score.append(R2)  
    summary2 = Model_name,Mean_squared_error,R2_score
    describe1 = pd.DataFrame(summary2[0],columns = {"Model_Name"})
    describe2 = pd.DataFrame(summary2[1],columns = {"Mean_squared_error"})
    describe3 = pd.DataFrame(summary2[2],columns = {"R2_score"})
    des = describe1.merge(describe2, left_index=True, right_index=True, how='inner')
    des = des.merge(describe3,left_index=True, right_index=True, how='inner')
    df = des.sort_values(ascending=False,by="R2_score").reset_index(drop = True)
    return(df)


# In[5]:

# summary_metrics()


# In[ ]:



