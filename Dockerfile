FROM python:3.7-alpine

EXPOSE 5000
WORKDIR /code

ADD requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=/code/wsgi.py


ADD . /code/