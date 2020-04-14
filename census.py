import unittest
import sqlite3
import json
import os

from bs4 import BeautifulSoup
import requests
import re
import csv

# base url for census 

base_url = 

conn = sqlite3.connect('')
cur = conn.cursor()

def setUpDatabase( ):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+ 'census.db')
    cur = conn.cursor()
    return cur, conn


cur.execute("CREATE TABLE IF NOT EXISTS Locations (address TEXT, data TEXT)")


# reads from data and adds data to the database

fh = open("  .data")



def create_request_url( ):

# getting data from the web 
# creating an api request with the request url 

    parms = 
    url =  base_url + parms
    r = requests.get(url)

    try:
        dict = json.loads(r.text)
    except:
        print("error when reading from url")  
        dict = {}

