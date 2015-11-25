#!/bin/bash

echo 'Updating system...'

# sudo apt-get update -y
# sudo apt-get upgrade -y

echo 'Installing dependencies...'

sudo apt-get install -y mysql-server libmysqlclient-dev
sudo apt-get install -y build-essential
sudo apt-get install -y python-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libffi-dev
sudo apt-get install -y libxml2-dev libxslt-dev libcurl4-openssl-dev
sudo apt-get install -y python-setuptools
sudo apt-get install -y libatlas-base-dev libatlas-dev liblapack-dev

sudo easy_install pip
sudo pip install -U virtualenv

echo 'Setting up virtualenv...'

virtualenv venv
. venv/bin/activate
pip install -U -r requirements.txt

deactivate

echo 'Done.'
