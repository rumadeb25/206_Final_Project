import unittest
import sqlite3
import json
import os

from bs4 import BeautifulSoup
import requests
import re
import csv
import codecs

conn = sqlite3.connect('census.db')
cur = conn.cursor()

# compare average income and health coverage per county/state 

cur.execute("SELECT * FROM Census")
income_list = []
coverage_list = []
for row in cur:
    income_data = row[3]
    income_list.append(income_data)
cur.execute("SELECT * FROM Insurance")
for row in cur:
    coverage_data = row[1]
    coverage_list.append(coverage_data)

fhand = codecs.open('compare_census.txt', 'w', "utf-8")
fhand.write("myData = [\n")
    
count = 0
for i in range(len(income_list)):
    count = count + 1
    if count > 1:
        fhand.write("\n")    
    output = str(income_list[i])+","+str(coverage_list[i])
    fhand.write(output)

fhand.write("\n];\n")
cur.close()
fhand.close()


