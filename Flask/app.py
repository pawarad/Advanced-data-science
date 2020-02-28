import os, zipfile
from flask import Flask, render_template, flash, request, url_for, redirect, Response, send_file,json
# from functions import credentials, read_file,model_run,zip_file,unzip_file,form_output
from os import remove,path
from werkzeug.utils import secure_filename
import json
import pandas as pd
import sys
# from ArimaFun import Stock_name
from Forecast import Stock_name
from flask_jsonpify import jsonpify
from pandas.io.json import json_normalize
import numpy as np
import time
import timestamp
from summarymetricsfunc import summary_metrics

globalVar = "abc"

app = Flask(__name__)
@app.route('/')
def homepage():
	# print("First Page")
	return render_template("main.html")



	# # import config as cg
	# app.config.update({
	# 	"STORAGE_PROVIDER": "S3", # Can also be S3, GOOGLE_STORAGE, etc... 
	# 	"STORAGE_KEY": "AKIAJQ7VKPEF3XSGEUIA",
	# 	"STORAGE_SECRET": "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",
	# 	"STORAGE_CONTAINER": "finalads",  # a directory path for local, bucket name of cloud
	# 	"STORAGE_SERVER": True,
	# #	"STORAGE_SERVER_URL": "/files" # The url endpoint to access files on LOCAL provider
	# })

	# # my_object = storage.get("accuracy.csv")
	# # my_new_path = "./downloads"
	# # my_new_file = my_object.save_to(my_new_path)

	# # Setup storage
	# storage = Storage()
	# storage.init_app(app) 

	# storage = Storage(S3, AKIAJQ7VKPEF3XSGEUIA, CTkdVK0ftphqlXoc4Y+kkOHs6nDw5PTQ/aFay4X4, finalads)
	# my_object = storage.get("accuracy.csv")
	# download_url = my_object.download_url("SummaryPage.html")	

	# A download endpoint, to download the file
	# @app.route("/download/<path:object_name>")
	# def download(object_name):
	# 	my_object = storage.get(object_name)
	# 	if my_object:
	# 		download_url = my_object.download_url()
	# 		return redirect(download_url)
	# 	else:
	# 		abort(404, "File doesn't exist")

	# @app.route('/SummaryPage/',methods=["Get","Post"])
	# def download(object_name):
	#     my_object = storage.get(object_name)
	#     if my_object:
	#     # Setup storage
	#         download_url = my_object.download()
	#         return redirect(download_url)
	#     else:
	#         abort(404, "File doesn't exist")



	# @app.route('/')
	# @app.route('/PredictionPage/', methods=["GET","POST"])
	# def PredictionPage():
	# #CompanyName=getStock_Company()
	# #To call the def of the function created hard coded
	# 	cmpynam = request.form["stock"]

	# 	cmpn = Stock_name(cmpynam)
	# 	#print("Second Page")
	#var2 = "image"+str(timestamp)+".png"
	plt.save(var4)
	return render_template('PredictionPage.html' , imagename=var4)
	# 	#important to understand
def getStock_Company():
	return render_template("PredictionPage.html")

def getStock_Company1():
	return render_template("SummaryPage.html")

# @app.route(/saveimage,methods=['POST'])
# def ranga():
# imgname="image"+str(timestamp)+".png"
# 	plt.save(imgname)
# 	return render("pagename.html",imgname=imgname)
# 	{{ filename=imgname}}


@app.route('/')
@app.route('/PredictionPage', methods=["POST"])
def PredictionPage():
	print('printing request')
	global globalVar
	globalVar = request.form['stock']
	print(globalVar)
	cmpn = Stock_name(globalVar)
	CompanyName=getStock_Company()
	getstock=Stock_name(globalVar)
	# print("Second Page")
	# print ('receiving data')
	# request.data
	# y = json.loads(request.data)
	# print (y)	
	# d1=getstock


	# df = pd.option_context('display.max_rows', None, 'display.max_columns', None)
	# print(df)
	df_list = getstock.values.tolist()
	# print(df_list)
	data = jsonpify(df_list)
	# df = pd.read_json(JSONP_data,orient='columns')
	# df = pd.DataFrame(np.array(df_list))
	print(type(data))
	vsr=os.path.join(os.getcwd(),"test.png")
	return render_template('PredictionPage.html', data=df_list,vsr=vsr)

		# return (td1) 



@app.route('/SummaryPage/', methods=["GET","POST"])
def SummaryPage():
	print("Third Page")
	# compnynam = request.form['stock']
	print("globalVar")
	print(globalVar)
	# cmpn1 = Stock_name(compnynam)
	CompanyName1=getStock_Company1()
	getstock1=summary_metrics(globalVar)

	df_list1 = getstock1.values.tolist()
	print(df_list1)
	data1 = jsonpify(df_list1)
	
	return render_template('SummaryPage.html',data=df_list1)	





@app.route('/Stocks/', methods=["GET","POST"])
def Stocks():
	print("Fourth Page")
	return render_template('Stocks.html')


if __name__ == "__main__":
	app.run()
