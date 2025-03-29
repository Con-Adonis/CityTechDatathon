import matplotlib.pyplot as plt
import csv

# Read data from the file
fileRead = open('OATH_Data_Lean.csv', 'r')
reader = csv.reader(fileRead)

boroughs = {
    'Manhattan': [],
    'Brooklyn': [],
    'Bronx': [],
    'Queens': [],
    'Staten Island': []
}

#Parse the file and organize data
a = reader
x = []
for i in a:
    x.append(i)

for i in range(len(x)):
    if i%3 == 0 or i%3 == 2:
        continue
    if int(i/3) == 0:
        for j in range(0, len(x[i]), 2): 
            boroughs['Manhattan'].append([x[i][j].split("(")[1].split("'")[1], int(x[i][j + 1].split(")")[0])])
    elif int(i/3) == 1:
        for j in range(0, len(x[i]), 2):
            boroughs['Brooklyn'].append([x[i][j].split("(")[1].split("'")[1], int(x[i][j + 1].split(")")[0])])
    elif int(i/3) == 2:
        for j in range(0, len(x[i]), 2):
            boroughs['Bronx'].append([x[i][j].split("(")[1].split("'")[1], int(x[i][j + 1].split(")")[0])])
    elif int(i/3) == 3:
        for j in range(0, len(x[i]), 2):
            boroughs['Queens'].append([x[i][j].split("(")[1].split("'")[1], int(x[i][j + 1].split(")")[0])])
    elif int(i/3) == 4:
        for j in range(0, len(x[i]), 2):
            boroughs['Staten Island'].append([x[i][j].split("(")[1].split("'")[1], int(x[i][j + 1].split(")")[0])])


fileRead.close()

#Plotting bar graphs for each borough
for borough, data in boroughs.items():
    if data:
        codes, counts = zip(*data)
        plt.figure(figsize=(10, 6))
        plt.bar(codes, counts, color='blue')
        plt.title(f"{borough}'s 20 Most Frequent Violations")
        plt.xlabel('Violation Code')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
