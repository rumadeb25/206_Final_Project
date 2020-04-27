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

def lifeExpTable():
    path = os.path.dirname(os.path.abspath(__file__)) + os.sep
    full_path = path + "/" + "Life_expect.csv"
    file_obj = open(full_path, "r") 
    r = csv.reader(file_obj)
    counties_list = []
    f_life_list = []
    m_life_list = []
    counties = []
    f_life = []
    m_life = []

    #cur.execute("DROP TABLE IF EXISTS Life_Expectancy")
    cur.execute("CREATE TABLE IF NOT EXISTS Life_Expectancy (county_num INTEGER, County TEXT, Female_Life_Expectancy INTEGER, Male_Life_Expectancy INTEGER)")
    topnum = len(cur.execute("SELECT * FROM Life_Expectancy").fetchall())
    bottomnum = topnum + 20

    for i in r:
        counties.append(i[0])
        counties_list = counties
        f_life.append(i[2])
        f_life_list = f_life
        m_life.append(i[3])
        m_life_list = m_life
    file_obj.close()


    x = 1
    y = 0
    for i in counties_list[topnum:bottomnum]:
        
        county_num = topnum + x
        j = topnum + y 

        #print(f_life_list[j])
    
        cur.execute("INSERT INTO Life_Expectancy (county_num, County, Female_Life_Expectancy, Male_Life_Expectancy) VALUES (?,?,?,?)",(county_num, i, f_life_list[j], m_life_list[j]))
        
        x += 1 
        y += 1

    conn.commit()

def main():
    lifeExpTable()
if __name__ == '__main__':
    main()