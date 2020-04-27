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

def medIncomeTable(): 
    path = os.path.dirname(os.path.abspath(__file__)) + os.sep
    full_path = path + "/" + "Unemployment.csv"
    file_obj = open(full_path, "r") 
    r = csv.reader(file_obj)
    counties_list = []
    income_list = []
    unemploy_list = []
    counties = []
    income = []
    umemploy = []

    # cur.execute("DROP TABLE IF EXISTS MedIncome")
    cur.execute("CREATE TABLE IF NOT EXISTS MedIncome (county_num INTEGER, County TEXT, Median_Income INTEGER, Unemployment INTEGER)")
    topnum = len(cur.execute("SELECT * FROM MedIncome").fetchall())
    bottomnum = topnum + 20

    for i in r:
        counties.append(i[2])
        counties_list = counties[6:]
        income.append(i[54])
        income_list = income[6:]
        umemploy.append(i[52])
        unemploy_list = umemploy[6:]

    file_obj.close()


    x = 1
    y = 0
    for i in counties_list[topnum:bottomnum]:
        
        county_num = topnum + x
        j = topnum + y 

        #print(income_list[j])
    
        cur.execute("INSERT INTO MedIncome (county_num, County, Median_Income, Unemployment) VALUES (?,?,?,?)",(county_num, i, income_list[j], unemploy_list[j]))
        
        x += 1 
        y += 1

    conn.commit()

def main():
    medIncomeTable()
if __name__ == '__main__':
    main()