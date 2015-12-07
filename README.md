# Product similarity analysis and categorization / clustering


> I am crawling an e commerce website (bukalapak) using Python scrapy. For a product, I hope to count the number of similar products on this site.
> The difficulty is to konw whether two products (with different icons and titles) are the same. Hope to find a data mining professional for this work.

## Installaion 

 1. install pip
 1.1. `sudo apt-get install python-setuptools python-dev build-essential`
 1.2. `sudo easy_install pip`
 2. Set-up *MySQL* client and make sure you can connect to the DB
 3. Run **./intall.sh** from the project directory
 4. Add to **PYTHON_PATH** the path to **site-aggregation** project, eg, `export PYTHON_PATH=$HOME/site-aggregation`
 5. Set the MySQL user password either in the configuration of *site-aggregation* project or using **MYSQL_PWD**, eg, `export MYSQL_PWD=******`
 6. Run **get_clusters.py** script (it might take a few minutes to run it)

