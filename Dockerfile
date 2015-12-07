# This is a comment
FROM ubuntu:14.04
MAINTAINER Rad Cirskis <nad2000@gmail.com>
RUN apt-get update && apt-get install -y mysql-server
RUN apt-get install -y python
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv

