import matplotlib 
import matplotlib.pyplot as plt
import sqlite3
import csv
import codecs

conn = sqlite3.connect('census.db')
cur = conn.cursor()

# compare median income and life expectancy per county

cur.execute("SELECT Life_Expectancy.Female_Life_Expectancy, Life_Expectancy.Male_Life_Expectancy, MedIncome.Median_Income FROM Life_Expectancy JOIN MedIncome ON Life_Expectancy.county_num = MedIncome.county_num")
joined = cur.fetchall()
fhand = codecs.open('comparison.txt', 'w', "utf-8")
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
cur.execute("SELECT Census.With_Coverage, Life_Expectancy.Female_Life_Expectancy, Life_Expectancy.Male_Life_Expectancy FROM Census JOIN Life_Expectancy ON Census.County = Life_Expectancy.County")




# cur.execute("SELECT Census.Median_Income, Insurance.With_Coverage,  FROM Census JOIN Insurance ON Census.county_num  ")
# cur.execute("CREATE TABLE IF NOT EXISTS Comparison (Life_Expectancy.Female_Life_Expectancy)")
# cur.execute("SELECT Restaurants.name, Restaurants.address FROM Restaurants JOIN Categories ON Restaurants.category_id = Categories.id WHERE Categories.title = ?",(category,))
# cur.execute("SELECT Restaurants.name FROM Restaurants JOIN Categories ON Restaurants.category_id = Categories.id WHERE Restaurants.price = ? AND Restaurants.rating >= ? AND Categories.title = ?",(price, rating, category))


