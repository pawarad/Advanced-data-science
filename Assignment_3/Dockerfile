FROM python:latest
RUN mkdir -p /usr/local/src/flask
WORKDIR /usr/local/src/flask

RUN mkdir -p static
RUN mkdir -p templates
RUN mkdir -p Output

ADD app2.py .
ADD functions.py .
ADD Usernames.txt .
ADD static static/.
ADD Templates templates/.
ADD Models Models/.
RUN pip install flask
RUN pip install pandas
RUN pip install sklearn
RUN pip install scipy
RUN pip install boto
EXPOSE 80
CMD ["sh","-c","python /usr/local/src/flask/app2.py"]
