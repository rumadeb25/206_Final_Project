import matplotlib 
import matplotlib.pyplot as plt
import sqlite3
import csv
import codecs

conn = sqlite3.connect('census.db')
cur = conn.cursor()

# compare average income and health coverage per county in Alabama
cur.execute("SELECT * FROM Census")
alabama_income = []
alabama_coverage = []
for row in cur: 
    state = row[2]
    if state == " Alabama":
        alabama_income.append(row[3])
        alabama_coverage.append(row[4])

# write data to alabama text file 
fhand = codecs.open('alabama.txt', 'w', "utf-8")
fhand.write("AlabamaData = [\n")
    
count = 0
for i in range(len(alabama_income)):
    count = count + 1
    if count > 1:
        fhand.write("\n")    
    output = str(alabama_income[i])+","+str(alabama_coverage[i])
    fhand.write(output)

fhand.write("\n];\n")
fhand.close()



# compare average income and health coverage per county in Michigan
cur.execute("SELECT * FROM Census")
michigan_income = []
michigan_coverage = []
for row in cur: 
    state = row[2]
    if state == " Michigan":
        michigan_income.append(row[3])
        michigan_coverage.append(row[4])

# write data to michigan text file 
fhand = codecs.open('michigan.txt', 'w', "utf-8")
fhand.write("MichiganData = [\n")
    
count = 0
for i in range(len(michigan_income)):
    count = count + 1
    if count > 1:
        fhand.write("\n")    
    output = str(michigan_income[i])+","+str(michigan_coverage[i])
    fhand.write(output)

fhand.write("\n];\n")
fhand.close()

cur.close()



# scatterplot for Alabama
with open('alabama.txt') as f:
    lines = f.readlines()
    income = [line.split(',')[0] for line in lines[1:-1]]
    coverage = [line.split(',')[1] for line in lines[1:-1]]
    coverage = list(map(str.strip, coverage))
    #import pdb; pdb.set_trace()
    
plt.figure()
plt.scatter(income, coverage)
plt.xlabel("Median Income")
plt.ylabel("Num People with Insurance Coverage")
plt.title('2010 Census Data Comparing Median Income and Insured Averages in Alabama')
f.close()



# scatterplot for Michigan
with open('michigan.txt') as f:
    lines = f.readlines()
    income = [line.split(',')[0] for line in lines[1:-1]]
    coverage = [line.split(',')[1] for line in lines[1:-1]]
    coverage = list(map(str.strip, coverage))
    #import pdb; pdb.set_trace()
    
plt.figure()
plt.scatter(income, coverage)
plt.xlabel("Median Income")
plt.ylabel("Num People with Insurance Coverage")
plt.title('2010 Census Data Comparing Median Income and Insured Averages in Michigan')
f.close()

plt.show()





