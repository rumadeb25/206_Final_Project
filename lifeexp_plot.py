import matplotlib 
import matplotlib.pyplot as plt
import sqlite3
import csv
import codecs
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



conn = sqlite3.connect('census.db')
cur = conn.cursor()

# compare life expectancy, median income, and num unemployed per county
def lifeAndUnemployment():
    cur.execute("SELECT Life_Expectancy.Female_Life_Expectancy, Life_Expectancy.Male_Life_Expectancy, MedIncome.Median_Income, MedIncome.Unemployment FROM Life_Expectancy JOIN MedIncome ON Life_Expectancy.county_num = MedIncome.county_num")
    joined = cur.fetchall()
    fhand = codecs.open('lifeAndUnemp.txt', 'w', "utf-8")
    fhand.write("countyData = [\n")
    for item in joined: 
        count = 0
        female = item[0]
        male = item[1]
        income = item[2]
        unemployed = item[3]
        count = count + 1
        if count == 1:
            fhand.write("\n")    
            output = str(female)+","+str(male)+","+str(income)+","+str(unemployed)
            fhand.write(output)
    fhand.write("\n];\n")
    fhand.close()



# plot for life expectancy, median income per county
def plotLifeAndIncome():
    with open('lifeAndUnemp.txt') as f:
        lines = f.readlines()
        avgLife = []
        female = [line.split(',')[0] for line in lines[2:-1]]
        male = [line.split(',')[1] for line in lines[2:-1]]
        
        femaleFloat = []
        for item in female:
            femaleFloat.append(float(item))
        maleFloat = []
        for item2 in male:
            maleFloat.append(float(item2))
        
        avgLife = []
        for i in range(len(femaleFloat)):
            avgLife.append((femaleFloat[i] + maleFloat[i]) / 2)
            
        income = [line.split(',')[2] for line in lines[2:-1]]
        income = list(map(str.strip, income))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=avgLife, y=income, mode='markers', name = 'female'))
    fig.update_layout(title='Comparing Life Expectancies and Median Income per County', xaxis_title='Life Expectancy in Years', yaxis_title='Median Income')
    fig.show()
    f.close()


# writing to txt file for life exp female, male, insurance per county
def lifeAndCoverage():
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

    cur.close()



# plot for life exp female, male, insurance per county
def plotLifeAndCoverage():
    with open('lifeAndInsurance.txt') as f:
        lines = f.readlines()
        female = [line.split(',')[0] for line in lines[2:-1]]
        fcoverage = [line.split(',')[2] for line in lines[2:-1]]
        fcoverage = list(map(str.strip, fcoverage))
        male = [line.split(',')[1] for line in lines[2:-1]]
        mcoverage = [line.split(',')[2] for line in lines[2:-1]]
        mcoverage = list(map(str.strip, mcoverage))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=female, y=fcoverage, mode='markers', name = 'female'))
    fig.add_trace(go.Scatter(x=male, y=mcoverage, mode='markers', name = 'male'))
    fig.update_layout(title='Comparing Life Expectancies and Number of People with Insurance Coverage', xaxis_title='Life Expectancy in Years', yaxis_title='Num People with Health Insurance')
    fig.show()
    f.close()


def main():
    lifeAndUnemployment()
    lifeAndCoverage()
    plotLifeAndCoverage()
    plotLifeAndIncome()
if __name__ == '__main__':
    main()