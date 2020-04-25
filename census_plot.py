import matplotlib 
import matplotlib.pyplot as plt

with open('compare_census.txt') as f:
    lines = f.readlines()
    income = [line.split(',')[0] for line in lines[1:-1]]
    coverage = [line.split(',')[1] for line in lines[1:-1]]
    coverage = list(map(str.strip, coverage))
    #import pdb; pdb.set_trace()
    
plt.figure()
plt.scatter(income, coverage)
plt.xlabel("Median Income")
plt.ylabel("Num People with Insurance Coverage")
plt.title('2010 Census Data Comparing Median Income and Insured Averages by State')
plt.show()






