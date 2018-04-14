from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, json, send_file
from werkzeug.utils import secure_filename
import pandas as pd
import os
import boto3, botocore, time
from boto3.s3.transfer import S3Transfer
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import glob

import config as cg	
app = Flask(__name__)
s3 = boto3.client(
   "s3",
   aws_access_key_id=cg.S3_KEY,
   aws_secret_access_key=cg.S3_SECRET_ACCESS_KEY
)
def upload_file_to_s3(file, bucket_name, acl="public-read"):


    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e
    return secure_filename(file.filename)
@app.route('/')
def homepage():

	print("I am in homepage")
	return render_template("main.html")
	
@app.route('/dashboard/' , methods=["GET", "POST"])
def dashboard():
	print("dashhhhhhhhhhhhh")
	try:
		if request.method == "POST":
			attempted_username= request.form['username']
			attempted_password = request.form['password'] 
			if attempted_username == "team11" and attempted_password == "team11":
				return render_template("dashboard.html")
			else:
				error = "Invalid Credentails"
		return render_template("main.html" , error= error)		
	except Exception as e:
		return render_template("main.html" , error = error)
@app.route('/upload_csv/' , methods=["GET", "POST"])
def upload_csv():
	try:
		if request.method == "POST":
			return render_template("upload_csv.html")
		else:
			error = "Not Valid"
		return render_template("dashboard.html" , error= error)
	except:
		return render_template("dashboard.html" , error= error)
@app.route('/fill_form/' , methods=["GET", "POST"])
def fill_form():
	try:
		if request.method == "POST":
			return render_template("fill_form.html")
		else:
			error = "Not Valid"
		return render_template("dashboard.html" , error= error)
	except:
		return render_template("dashboard.html" , error= error)
@app.route('/restAPI_calls/' , methods=["POST"])		
def restAPI_calls():
	# A
    if "filename" not in request.files:
        return "No user_file key in request.files"

	# B
    file = request.files["filename"]

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    if file:
        
        filename = secure_filename(file.filename)
        dir_name = 'uploads/'
        if not os.path.exists(dir_name):
        	os.makedirs(dir_name)
        file_path = os.path.join(dir_name, filename)
        file.save(file_path)
        try:

	        output = upload_file_to_s3(file, cg.S3_BUCKET)
	        print(output)
	        data = pd.read_csv(file_path)
        	conn = S3Connection(cg.S3_KEY, cg.S3_SECRET_ACCESS_KEY)
        	b = conn.get_bucket(cg.S3_BUCKET)
        	for obj in b.get_all_keys():
        		trial = obj.get_contents_to_filename(obj.key)
        	allFiles = glob.glob("/.csv")
        	print("entered glob")
        	for files in allFiles:
        		df = pd.read_csv( files ,index_col=None, header=0)
        	print(df);


        	return render_template("success.html")
        except:
        	
        	return render_template("upload_csv.html")

    else:
    	return render_template("404.html")
    return render_template("success.html")

if __name__ == "__main__":
    app.run()