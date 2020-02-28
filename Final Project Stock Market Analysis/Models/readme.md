
# STOCK PRICE FORECASTING

## Introduction
Predicting the stock price trend by interpreting the seemly chaotic market data has always been an attractive topic to both investors and researchers. Among those popular methods that have been employed, Machine Learning techniques are very popular due to the capacity of identifying stock trend from massive amounts of data that capture the underlying stock price dynamics. 

## Data Cleaning 
1. Removed irrelevant columns.
2. Data manipulation reseting the index and removing it whenever needed.

## Models 
1. ARIMA
2. Linear regression
3. Random Forest regressor

Among these 3 models linear regression gave the best summary metrics in terms of accuracy.

## Forecasting
Forecasted stock price for different types of stock tickers and weeks to be forecasted.

## Flask App
Deployed web application using flask in python where user inputs company ticker and gets relevant forecast information along with accuracy metrics and interactive graphical visualisation using plotly.

## EC2 Instance of the app
ec2-34-227-25-183.compute-1.amazonaws.com

