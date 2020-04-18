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
tuple_list = []
counties = []
income = []
insurance = []
for i in reader:
    counties.append(i[1])
    counties_list = counties[2:]
    income.append(i[250])
    income_list = income[2:]
    insurance.append(i[382])
    insurance_list = insurance[2:]
file_obj.close()

cur.execute("CREATE TABLE IF NOT EXISTS Census (county_num INTEGER, County TEXT, Median_Income INTEGER, With_Health_Insurance INTEGER)")
count = 0
for i in range(len(counties_list)):

    if count > 20 :
        print('Stored 20 items, restart to retrieve more')
        break

    county_num = i

    # write something so that duplicate data isnt stored
    # try:
    #     data = cur.fetchone()[0]
    #     print("Found in database ",address)
    #     continue
    # except:
    #     pass

    cur.execute("INSERT INTO Census (county_num, County, Median_Income, With_Health_Insurance) VALUES (?,?,?,?)",(county_num, counties_list[i], income_list[i], insurance_list[i]))
    
    count = count + 1

conn.commit()

# second table w shared key?
# cur.execute("CREATE TABLE IF NOT EXISTS