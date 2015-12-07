#!/bin/bash

MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# echo 'Updating system...'
# sudo apt-get update -y
# sudo apt-get upgrade -y

echo 'Installing dependencies...'

sudo apt-get install -y mysql-server
sudo apt-get install -y libmysqlclient-dev
sudo apt-get install -y build-essential
sudo apt-get install -y python-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libffi-dev
sudo apt-get install -y libxml2-dev libxslt-dev libcurl4-openssl-dev
sudo apt-get install -y python-setuptools
sudo apt-get install -y python-pip
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libatlas-dev
sudo apt-get install -y liblapack-dev
sudo apt-get install -y python-numpy
sudo apt-get install -y python-scipy

sudo pip install -U pip
sudo pip install -U virtualenv

echo 'Setting up virtualenv...'

virtualenv --system-site-packages venv
. venv/bin/activate
pip install -U -r ${MY_DIR}/requirements.txt

deactivate

echo 'Done.'
