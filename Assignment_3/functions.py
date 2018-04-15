import pandas as pd
import numpy as np
import pickle
import urllib.request
import sklearn
from sklearn.cross_validation import train_test_split 
from sklearn.ensemble import RandomForestRegressor
#from sklearn import linear_model
from sklearn.metrics import *
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB 
#from sklearn.neural_network import MLPRegressor
#from sklearn.svm import SVR
#from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
import shutil
import logging 
import boto.s3
from boto.s3.key import Key

def credentials():
    credentials = {}
    with open('Usernames.txt', 'r') as f:
    	for line in f:
      	  user, pwd, url = line.strip().split(';')
      	  lst=[pwd,url]
      	  credentials[user] = lst
    	return credentials

def read_file(path):
    df=pd.read_csv(path)
    return df

def col_selected():
    column_list1=['V1','V2','V3','V4','V5','V6','V7','V9','V10','V11','V12','V14','V16','V17','V18','V19','V21']
    return column_list1
    
def zip_file(a):
    shutil.make_archive(a,'zip',a)

def unzip_file(a,b):
    shutil.unpack_archive(a,extract_dir=b)

def del_directory(a):
    shutil.rmtree(a)

def form_output(dff):
    rfc=0
    Logreg=0
    NB=0
    y=[]
    x=pd.DataFrame(data=[dff],columns=col_selected())
    scaler = StandardScaler()
    scaler.fit(x)
    x_test_sc=scaler.transform(x)
    print(x.shape)
    filename = 'Models/rfc_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    rfc=np.round(mod.predict(x_test_sc),0)
	
    filename = 'Models/logreg_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    Logreg=np.round(mod.predict(x_test_sc),0)
	
    filename = 'Models/NB_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    NB=np.round(mod.predict(x_test_sc),0)
    y=[rfc,Logreg,NB] 
    df=pd.DataFrame(data=[y],columns=['Random Forest Classifier','Logistic Regression','Naive Bayes '])
    return x,df

def model_run(df):
    #df.columns=pd.DataFrame(data=dff,columns=header_col())
    #df.columns=header_col()
    print (df.shape)
    scaler = StandardScaler()
    x=df[col_selected()]
    print(x.head())
    scaler.fit(x)
    x_test_sc=scaler.transform(x)
    print(x.shape)
    d1=df.copy()
    filename = 'Models/rfc_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    d1['Target_variable']=mod.predict(x_test_sc)
    d1['Target_variable']=d1['Target_variable'].round(decimals=0)
    d1.to_csv('Output/Random_Forest_Classifier.csv',sep=',',index=False)
	
    d2=df.copy()
    filename = 'Models/logreg_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    d2['Target_variable']=mod.predict(x_test_sc)
    d2['Target_variable']=d2['Target_variable'].round(decimals=0)
    d2.to_csv('Output/Log_reg.csv',sep=',',index=False)
	
    d3=df.copy()
    filename = 'Models/NB_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    d3['Target_variable']=mod.predict(x_test_sc)
    d3['Target_variable']=d3['Target_variable'].round(decimals=0)
    d3.to_csv('Output/NB.csv',sep=',',index=False)
	
    
    d6=pd.read_csv("Models/accuracy_error_metrics.csv")
    #del_directory('Models')
    zip_file('Output')
    return d1,d6

def rest_run(df):
    #df.columns=pd.DataFrame(data=dff,columns=header_col())
    #df.columns=header_col()
    print (df.shape)
    scaler = StandardScaler()
    x=df[col_selected()]
    print(x.head())
    scaler.fit(x)
    x_test_sc=scaler.transform(x)
    print(x.shape)
    d1=df.copy()
    filename = 'Models/rfc_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    d1['Target_variable']=mod.predict(x_test_sc)
    d1['Target_variable']=d1['Target_variable'].round(decimals=0)
    d1.to_csv('Output/Random_Forest_Classifier.csv',sep=',',index=False)
	
    d2=df.copy()
    filename = 'Models/logreg_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    d2['Target_variable']=mod.predict(x_test_sc)
    d2['Target_variable']=d2['Target_variable'].round(decimals=0)
    d2.to_csv('Output/Log_reg.csv',sep=',',index=False)
	
    d3=df.copy()
    filename = 'Models/NB_model.pckl'
    mod = pickle.load(open(filename, 'rb'))
    d3['Target_variable']=mod.predict(x_test_sc)
    d3['Target_variable']=d3['Target_variable'].round(decimals=0)
    d3.to_csv('Output/NB.csv',sep=',',index=False)
	
    d6=pd.read_csv("Models/accuracy_error_metrics.csv")
    zip_file('Output')
    return d1,d6
