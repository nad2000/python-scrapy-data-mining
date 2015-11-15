#!/usr/bin/env python
import requests
from BeautifulSoup import BeautifulSoup
import nltk 
import sys
import csv

requests.packages.urllib3.disable_warnings()

def retrieve(url,prod_id=None):
    """
    Retrievs a single product page and extacts
    from it the product name and its description
    """
    res = requests.get(url, verify=False)
    
    soup = BeautifulSoup(res.text)
    title = soup.find("h1", attrs={"class": "product-detailed__name"}).text
    description = soup.find("div", id=lambda v: v and v.startswith("product_desc_")).text
    
    if title and description:
        print "{0}\t{1}\t{2}\t{3}".format(url, title, description, prod_id)

if len(sys.argv) > 1 and sys.argv[1].startswith("http"):
    url = sys.argv[1]
    retrieve(url)
else:
    if len(sys.argv) > 1:
        raw = open(sys.argv[1], 'r')
    else:
        raw = sys.stdin

    for (prod_id, url) in csv.reader(raw):
        try:
            retrieve(url, prod_id)
        except Exception as e:
            sys.stderr.write(e)
            pass
