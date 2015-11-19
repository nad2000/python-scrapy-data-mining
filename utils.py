import dill
import nltk
from stem import IndonesianStemmer
import string
import os
import re
from collections import defaultdict
import multiprocessing
import dill
import csv
import string
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from id_stopwords import stopwords
import math

# Location of category product similarity files:
data_dir = "/data/python-scrapy-data-mining/"

stemmer = IndonesianStemmer()
# Include digits since it is important for product distinciont (eg a model number or version number):
tokenizer = nltk.tokenize.RegexpTokenizer("[\w'0-9]+|\$[\d\.]+|\S+", flags=re.UNICODE)

categories = None

def backup_object(obj, file_name=None):
    if file_name is None:
        file_name = "{0}.pkl".format(id(obj))
        print "*** Object stored in:", file_name
    with open(file_name, "wb") as bf:
        dill.dump(obj, bf)

        
def norm(vect):
    return math.sqrt(sum((v * v for v in vect.values())))


def distance(v1, v2):
    v1, n1 = v1[:2]
    v2, n2 = v2[:2] 
    dist = sum((v1[w] * v2[w] for w in set(v1).intersection(v2)), 0.0)
    return dist / (n1 * n2)

        
def restore_object(file_name):
    with open(file_name, "rb") as bf:
        return dill.load(bf)


def chunks(l, num):
    """
    splits list in num chunks
    for running in parallel
    """
    n = len(l) / num + 1
    return [l[i:i + n] for i in range(0, len(l), n)]


def tokenize_and_stem_ID(text):
    """
    Tokenize and stem Indonesian text
    """
    global stemmer, tokenizer
    return [stemmer.stem(token) for token in tokenizer.tokenize(text)]


def get_categories():

    global categories

    if categories is None:
      
        # Product categorie list:
        with open(os.path.join(data_dir, "urls.csv")) as raw:
            categories = list(set(('/'.join(parts[4:-1]) for parts in (url[1].split('/') for url in csv.reader(raw))
                    if parts[3] == 'p')))

    return categories