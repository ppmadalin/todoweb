FROM python:3.7-slim

MAINTAINER Madalin Popa, contact@madalinpopa.com

# update 
RUN apt-get update

# install sqlite and mysql
RUN apt-get -y install sqlite mysql-server

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

# create user and database within mysql
# RUN /etc/init.d/mysqld start
# RUN mysql -h 127.0.0.1 -P 3306 --protocol=tcp -u root -p < /opt/todoweb/dbinit.sql

# migrate database
# RUN flask db migrate
# RUN flask db upgrade

# Listen to port 80 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD ["flask", "run", "--host", "0.0.0.0"]
