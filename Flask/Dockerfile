FROM python : 3
RUN mkdir -p C:/Users/Ranga Chari/Documents/GitHub/Final_Project-/Flask
WORKDIR C:/Users/Ranga Chari/Documents/GitHub/Final_Project-/Flask

RUN mkdir -p static
RUN mkdir -p templates

ADD app.py .
ADD summarymetricsfunc.py .
ADD Forecast.py .
ADD static static/.
ADD Templates templates/.
RUN pip3 install flask
RUN pip3 install pandas
RUN pip3 install scipy
RUN pip3 install boto
RUN pip3 install matplotlib
RUN pip3 install datetime
Run pip3 install imblearn
Run pip3 install seaborn
Run pip3 install pickle
Run pip3 install requests
Run pip3 install boto3
Run pip3 install plotly
Run pip3 install flask_jsonpify
Run pip3 install math

EXPOSE 80

CMD ["sh","-c","python .Github/Final_Project-/Flask/app.py"]
ENTRYPOINT ["python","./app.py"]
