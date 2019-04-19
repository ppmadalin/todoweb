FROM python:3.7-slim

MAINTAINER Madalin Popa, contact@madalinpopa.com

# update 
RUN apt-get update

# install sqlite
RUN apt-get -y install sqlite

# make a local directory
RUN mkdir /opt/todoweb

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/todoweb

# copy requirements.txt to /app
ADD requirements.txt .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# now copy all the files in this directory to /code
ADD . .

# Listen to port 80 at runtime
EXPOSE 5000

ENV FLASK_APP=manage.py
ENV FLASK_ENV=development
ENV SECRET_KEY=secret

# Initiate database
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Define our command to be run when launching the container
CMD ["flask", "run", "--host", "0.0.0.0"]