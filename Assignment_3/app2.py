import os, zipfile
from flask import Flask, render_template, flash, request, url_for, redirect, Response, send_file
from functions import credentials, read_file,model_run,zip_file,unzip_file,form_output
from os import remove,path
from werkzeug.utils import secure_filename
import json
import pandas as pd
import sys

#ak=sys.argv[1]
#sak=sys.argv[2]

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='Data'
# set as part of the config
SECRET_KEY = 'many random bytes'
app.config['S3']=''
# or set directly on the app
app.secret_key = 'many random bytes'
@app.route('/')
def homepage():
    print("main hiiiii")
    return render_template("main.html")

#@app.route('/login/')
#def login():
#    return render_template("dashboard.html")

@app.route('/dashboard/', methods=["GET","POST"])
def dashboard():
    print("dashboard hiiiiiiiiiii")
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            #flash(attempted_username)
            #flash(attempted_password)
            credt=credentials()
            lst=credt[attempted_username]
            if attempted_username in credt and lst[0]==attempted_password:
            #if attempted_username == "admin" and attempted_password == "password":
                print("sucess!!!!")
                #return render_template("dashboard.html")
                #return redirect(url_for('login'))
                return render_template("dashboard.html")
            else:
                error = "Invalid credentials. Try Again."
                print(error)
                flash(error)
        return render_template("main.html", error = error)
    except Exception as e:
        #flash(e)
        print(e)
        return render_template("main.html", error = error)

@app.route('/upload/', methods=['GET','POST'])
def upload_file(): 
    print("upload hiiiiiiiiiii")
    error = ''
#    os.remove('Output.zip')
    try:
        if request.method == 'POST':
           f=request.files['file']
           f.save(secure_filename(f.filename))
           df=read_file(f.filename)
           df1,df_summ=model_run(df)
           #df.to_csv('predictoutput.zip',sep=',',index=False)
           os.remove(f.filename)
           return render_template("view.html",tables=[df_summ.to_html(),df1.to_html()], titles = ['Error Metrics','Predicted O/P'])
           #return render_template("view.html",name='Predicted O/P', tables=[df_summ.to_html(),df1.to_html()], titles = ['Error Metrics','Predicted O/P'])
           #jsonfiles = json.loads(df.head().to_json(orient='records'))
           #return render_template('view.html', ctrsuccess=jsonfiles)
           #tables=[df.to_html(classes='dataframe')], titles = ['na', 'Predicted O/P'])
           #flash("File uploaded")
        error = "File Not uploaded"
        return render_template("dashboard.html", error = error)
    except Exception as e:
        #flash(e)
        print(e)
        return render_template("dashboard.html", error = error)

@app.route('/forminput/', methods=['GET','POST'])
def form_input():
    print("form input")
    error = ''
    try:
        if request.method == 'POST':
           V1=request.form['V1']
           V2=request.form['V2']
           V3=request.form['V3']
           V4=request.form['V4']
           V5=request.form['V5']
           V6=request.form['V6']
           V7=request.form['V7']
           V9=request.form['V9']
           V10=request.form['V10']
           V11=request.form['V11']
           V12=request.form['V12']
           V14=request.form['V14']
           V16=request.form['V16']
           V17=request.form['V17']
           V18=request.form['V18']
           V19=request.form['V19']
           V21=request.form['V21']

           x=[V1,V2,V3,V4,V5,V6,V7,V9,V10,V11,V12,V14,V16,V17,V18,V19,V21]
           #df=pd.DataFrame(x)
           df,df_out=form_output(x)
           return render_template("formout.html",tables=[df.to_html(),df_out.to_html()], titles = ['Inputs Given','O/p Predicted by different Models'])
        error= " Invalid Inputs"
        return render_template("dashboard.html", error = error)
    except Exception as e:
        #flash(e)
        print(e)
        return render_template("dashboard.html", error = error)
   
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/getCSV/')
def getCSV():
    try:
        file_path=os.path.join(app.root_path,'Output.zip')
        #rchive = zipfile.ZipFile('Output.zip', 'r')
        return send_file(file_path, attachment_filename='predictedoutpt.zip',as_attachment=True)
        #return Response(archive,mimetype="application/zip",headers={"Content-disposition":"attachment; filename=Output.zip"})
    except Exception as e:
        return str(e)

@app.route('/predictoutput/', methods=['POST'])
def PredictOutput():
    #return request.data
    data = request.get_json(force=True)
    df = pd.io.json.json_normalize(data)
    print(df)
    js=json.loads(df.head().to_json(orient='records'))
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    #resp.headers['Link'] = 'http://luisrei.com'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
