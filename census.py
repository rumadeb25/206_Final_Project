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
cur.execute("CREATE TABLE IF NOT EXISTS Census (county_num INTEGER, County TEXT, State TEXT, Median_Income INTEGER, With_Health_Insurance INTEGER)")

# the number of items in the table already
topnum = len(cur.execute("SELECT * FROM Census").fetchall())
# the number of items in the table + 20 
bottomnum = topnum + 20

state_list = []
final_county_list = []

for i in reader:
    counties.append(i[1])
    counties_list = counties[2:-1]
    income.append(i[250])
    income_list = income[2:-1]
    insurance.append(i[382])
    insurance_list = insurance[2:-1]

for item in counties_list:
    split = item.split(',')
    county = split[0]
    state = split[1]
    final_county_list.append(county)
    state_list.append(state)
#import pdb; pdb.set_trace()
    
file_obj.close()

x = 1
y = 0

# # to only add 20 at a time, only loop from the count of last item in the table to the item that is 20 counts away
for i in counties_list[topnum:bottomnum]:
    
    county_num = topnum + x
    indexer = topnum + y 
   
    cur.execute("INSERT INTO Census (county_num, County, State, Median_Income, With_Health_Insurance) VALUES (?,?,?,?,?)",(county_num, final_county_list[indexer], state_list[indexer], income_list[indexer], insurance_list[indexer]))
    
    x = x + 1; y = y + 1

conn.commit()

# second table w shared key
#cur.execute("DROP TABLE IF EXISTS Insurance")
cur.execute("CREATE TABLE IF NOT EXISTS Insurance (county_num INTEGER, With_Coverage INTEGER, Private_Health_Insurance INTEGER, Public_Health_Insurance INTEGER, No_Coverage INTEGER)")
top = len(cur.execute("SELECT * FROM Insurance").fetchall())
bottom = top + 20

fle_obj = open("census_data.csv", "r") 
read = csv.reader(fle_obj)
wc = []
with_coverage = []
priv = []
private = []
pub =[]
public = []
nc = []
no_coverage = []

for i in read:
    wc.append(i[382])
    priv.append(i[386])
    pub.append(i[390])
    nc.append(i[394])
    with_coverage = wc[2:]
    private = priv[2:]
    public = pub[2:]
    no_coverage = nc[2:]
fle_obj.close()

#import pdb; pdb.set_trace()

a = 1
z = 0
for i in counties_list[top:bottom]:
    
    county_num = top + a
    index = top + z 
   
    cur.execute("INSERT INTO Insurance (county_num, With_Coverage, Private_Health_Insurance, Public_Health_Insurance, No_Coverage) VALUES (?,?,?,?,?)",(county_num, with_coverage[index], private[index], public[index], no_coverage[index]))

    z  = z + 1; a = a + 1

conn.commit()

