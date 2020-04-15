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
lnes = file_obj.readlines()[2:]
counties_list = []
income_list = []
insurance_list = []
for i in lnes:  
    counties_list.append(i[1].strip())
    income_list.append(i[250])
    insurance_list.append(i[382])
file_obj.close()


cur.execute("CREATE TABLE IF NOT EXISTS Census (county_num INTEGER, county TEXT, income INTEGER, insurance TEXT)")
for i in range(len(counties_list)):
    county_num = i
    for i in counties_list:
        county = i
    for i in income_list:
        income = i
    for i in insurance_list:
        insurance = i
    cur.execute("INSERT INTO Census (county_num, county, income, insurance) VALUES (?,?,?,?)",(county_num, county, income, insurance))
conn.commit()
