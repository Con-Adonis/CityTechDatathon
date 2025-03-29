OATHfile = open('OATH_Data_Lean.csv', 'w')

#CSVs were downloaded locally based on each borough for the sake of easier filtering and downloading ease
readMann = open('/Users/connorkavleski/Downloads/OATH-ManhattanData.csv', 'r')
readBrkl = open('/Users/connorkavleski/Downloads/OATH-Brooklyn.csv', 'r')
readBronx = open('/Users/connorkavleski/Downloads/OATH-Bronx.csv', 'r')
readQueens = open('/Users/connorkavleski/Downloads/OATH-Queens.csv', 'r')
readSI = open('/Users/connorkavleski/Downloads/OATH-Staten.csv', 'r')


#Manhattan
MannDict = {}
count = 0
for line in readMann:
    lineSplit = line.split(',')
    #these specific orgs had a different filing system
    if len(lineSplit) < 39 or 'DOHMH' in lineSplit[3] or 'DEP - BUREAU OF ENV. COMPLIANC' in lineSplit[3] or 'DOHMH' in lineSplit[3]:
        continue
    #38 fields in csv until violation code is reached
    if len(lineSplit[38]) == 4:
        if lineSplit[38] not in MannDict:
            MannDict[lineSplit[38]] = 1
        else:
            MannDict[lineSplit[38]] += 1

OATHfile.write("Manhattan's 20 most frequent violations\n")
OATHfile.write(str(sorted(MannDict.items(), key=lambda x: x[1], reverse=True)[:20]))
OATHfile.write('\n\n')


#Brooklyn
BrklnDict = {}
count = 0
for line in readBrkl:
    lineSplit = line.split(',')
    #these specific orgs had a different filing system
    if len(lineSplit) < 39 or 'DOHMH' in lineSplit[3] or 'DEP - BUREAU OF ENV. COMPLIANC' in lineSplit[3] or 'DOHMH' in lineSplit[3]:
        continue
    #38 fields in csv until violation code is reached
    if len(lineSplit[38]) == 4:
        if lineSplit[38] not in BrklnDict:
            BrklnDict[lineSplit[38]] = 1
        else:
            BrklnDict[lineSplit[38]] += 1

OATHfile.write("Brooklyn's 20 most frequent violations\n")
OATHfile.write(str(sorted(BrklnDict.items(), key=lambda x: x[1], reverse=True)[:20]))
OATHfile.write('\n\n')


#Bronx
BronxDict = {}
count = 0
for line in readBronx:
    lineSplit = line.split(',')
    #these specific orgs had a different filing system
    if len(lineSplit) < 39 or 'DOHMH' in lineSplit[3] or 'DEP - BUREAU OF ENV. COMPLIANC' in lineSplit[3] or 'DOHMH' in lineSplit[3]:
        continue
    #38 fields in csv until violation code is reached
    if len(lineSplit[38]) == 4:
        if lineSplit[38] not in BronxDict:
            BronxDict[lineSplit[38]] = 1
        else:
            BronxDict[lineSplit[38]] += 1

OATHfile.write("Bronx's 20 most frequent violations\n")
OATHfile.write(str(sorted(BrklnDict.items(), key=lambda x: x[1], reverse=True)[:20]))
OATHfile.write('\n\n')


#Queens
QueensDict = {}
count = 0
for line in readQueens:
    lineSplit = line.split(',')
    #these specific orgs had a different filing system
    if len(lineSplit) < 39 or 'DOHMH' in lineSplit[3] or 'DEP - BUREAU OF ENV. COMPLIANC' in lineSplit[3] or 'DOHMH' in lineSplit[3]:
        continue
    #38 fields in csv until violation code is reached
    if len(lineSplit[38]) == 4:
        if lineSplit[38] not in QueensDict:
            QueensDict[lineSplit[38]] = 1
        else:
            QueensDict[lineSplit[38]] += 1

OATHfile.write("Queen's 20 most frequent violations\n")
OATHfile.write(str(sorted(QueensDict.items(), key=lambda x: x[1], reverse=True)[:20]))
OATHfile.write('\n\n')


#Staten Island
StatDict = {}
count = 0
for line in readSI:
    lineSplit = line.split(',')
    #these specific orgs had a different filing system
    if len(lineSplit) < 39 or 'DOHMH' in lineSplit[3] or 'DEP - BUREAU OF ENV. COMPLIANC' in lineSplit[3] or 'DOHMH' in lineSplit[3]:
        continue
    #38 fields in csv until violation code is reached
    if len(lineSplit[38]) == 4:
        if lineSplit[38] not in StatDict:
            StatDict[lineSplit[38]] = 1
        else:
            StatDict[lineSplit[38]] += 1

OATHfile.write("Staten Island's 20 most frequent violations\n")
OATHfile.write(str(sorted(StatDict.items(), key=lambda x: x[1], reverse=True)[:20]))
OATHfile.write('\n\n')