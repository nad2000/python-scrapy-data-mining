# Product similarity analysis and categorization / clustering

## Installaion 

 1. install pip: `sudo apt-get install python-pip python-dev build-essential; sudo pip install --upgrade pip`
 2. Set-up *MySQL* client and make sure you can connect to the DB
 3. Run **./intall.sh** from the project directory

## Building Product Clusters

 1. Add to **PYTHON_PATH** the path to **site-aggregation** project, eg, `export PYTHON_PATH=$HOME/site-aggregation`
 2. Set the MySQL user password either in the configuration of *site-aggregation* project or using **MYSQL_PWD**, eg, `export MYSQL_PWD=******`
 3. Run **get_clusters.py** script (it might take a few minutes to run it)

