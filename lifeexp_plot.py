import matplotlib 
import matplotlib.pyplot as plt
import sqlite3
import csv
import codecs

conn = sqlite3.connect('census.db')
cur = conn.cursor()

# compare life expectancy, median income, and num unemployed per county
cur.execute("SELECT Life_Expectancy.Female_Life_Expectancy, Life_Expectancy.Male_Life_Expectancy, MedIncome.Median_Income FROM Life_Expectancy JOIN MedIncome ON Life_Expectancy.county_num = MedIncome.county_num")
joined = cur.fetchall()
fhand = codecs.open('lifeAndUnemp.txt', 'w', "utf-8")
fhand.write("countyData = [\n")
for item in joined: 
    count = 0
    female = item[0]
    male = item[1]
    income = item[2]
    count = count + 1
    if count == 1:
        fhand.write("\n")    
        output = str(female)+","+str(male)+","+str(income)
        fhand.write(output)
fhand.write("\n];\n")
fhand.close()



conn = sqlite3.connect('census.db')
cur = conn.cursor()

# life exp female, male, insurance per county
cur.execute("SELECT Life_Expectancy.Female_Life_Expectancy, Life_Expectancy.Male_Life_Expectancy, Census.With_Health_Insurance FROM Census JOIN Life_Expectancy ON Census.County = Life_Expectancy.County")
compiled = cur.fetchall()
fhand = codecs.open('lifeAndInsurance.txt', 'w', "utf-8")
fhand.write("countyData = [\n")
for item in compiled: 
    count = 0
    female = item[0]
    male = item[1]
    insurance = item[2]
    count = count + 1
    if count == 1:
        fhand.write("\n")    
        output = str(female)+","+str(male)+","+str(insurance)
        fhand.write(output)
fhand.write("\n];\n")
fhand.close()