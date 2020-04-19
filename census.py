import unittest
import sqlite3
import json
import os

from bs4 import BeautifulSoup
import requests
import re
import csv

conn = sqlite3.connect('census.db')
cur = conn.cursor()

# reads from data and adds data to the database

file_obj = open("census_data.csv", "r") 
reader = csv.reader(file_obj)
counties_list = []
income_list = []
insurance_list = []
counties = []
income = []
insurance = []

#cur.execute("DROP TABLE IF EXISTS Census")
cur.execute("CREATE TABLE IF NOT EXISTS Census (county_num INTEGER, County TEXT, Median_Income INTEGER, With_Health_Insurance INTEGER)")
topnum = len(cur.execute("SELECT * FROM Census").fetchall())
bottomnum = topnum + 20

for i in reader:
    counties.append(i[1])
    counties_list = counties[2:]
    income.append(i[250])
    income_list = income[2:]
    insurance.append(i[382])
    insurance_list = insurance[2:]
file_obj.close()

x = 1
y = 0
for i in counties_list[topnum:bottomnum]:
    
    county_num = topnum + x
    indexer = topnum + y 
   
    cur.execute("INSERT INTO Census (county_num, County, Median_Income, With_Health_Insurance) VALUES (?,?,?,?)",(county_num, i, income_list[indexer], insurance_list[indexer]))
    
    x = x + 1; y = y + 1

conn.commit()

# second table w shared key?
# cur.execute("CREATE TABLE IF NOT EXISTS