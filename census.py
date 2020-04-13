import unittest
import sqlite3
import json
import os

from bs4 import BeautifulSoup
import requests
import re
import csv

#base census url 
base_url = 

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# def setUpDatabase(db_name):
#     path = os.path.dirname(os.path.abspath(__file__))
#     conn = sqlite3.connect(path+'/'+db_name)
#     cur = conn.cursor()
#     return cur, conn

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')


#reads from data and adds data to the database

fh = open("where.data")





#getting data from the web 
#creating an api request with the request url 
parms = dict()
parms["address"] = address
url =  base_url + parms

r = requests.get(url)

try:
    dict = json.loads(r.text)
except:
    print("error when reading from url")  
    continue


# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
# count = count + 1 