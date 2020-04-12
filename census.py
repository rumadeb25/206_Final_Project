import unittest
import sqlite3
import json
import os

#reads from .data and adds data to the database 
#

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#getting data from the web 
parms = dict()
parms["address"] = address 
if api_key is not False: parms['key'] = api_key
url =  serviceurl + urllib.parse.urlenconde(parms)
