import re
nearby = False
ruleZone = True
errRate = 0
with open('marcomole00/16/input.txt') as file:
    lines = file.read().split('\n')
    lines = list(map(str, lines))
rules = {}
wrongIndexes = []
myTicket = [101,179,193,103,53,89,181,139,137,97,61,71,197,59,67,173,199,211,191,131]
for line in lines:
    if line == '' or line == 'your ticket:' : 
        ruleZone = False
        continue
    if line == 'nearby tickets:' : 
        nearby = True
        continue
    if ruleZone == True:
        field, values = re.split(":", line)[0:2]
        values = re.split(' or ', values.strip(' '))
        for val in values:
            val = val.split('-')
            val = list(map(int, val))
            if field not in rules:
                rules[field] = [val]
            else: rules[field].append(val)
    elif nearby == True:
        
        numbers = line.split(',')
        for dig in numbers:
            valid = False
            if dig == ',': continue
            dig = int(dig)
            for key in rules:
                if (rules[key][0][0] <= dig <= rules[key][0][1]) or (rules[key][1][0] <= dig <= rules[key][1][1]):
                    valid = True
            if valid == False: 
                wrongIndexes.append(lines.index(line)-25) # remember to change this from test to input and vicecersa 8 to 25
                errRate += dig 

nearby = list(map(lambda line: line.split(','),lines[25:]))  # remember to change this from test to input and vicecersa 8 to 25
columns = {}

for key in rules:
    #if 'departure' not in key: continue
    columns[key] = []
    for j in range(len(nearby[0])):
        valid = 0
        for i in range(len(nearby)):
            if i in wrongIndexes: continue

            dig = int(nearby[i][j])
            if (rules[key][0][0] <= dig <= rules[key][0][1]) or (rules[key][1][0] <= dig <= rules[key][1][1]):
                valid +=1
        if valid == len(nearby)- len(wrongIndexes):
            columns[key].append(j)      
singleton = set()
for key in columns: print(columns[key])      
while True:
    if len(singleton) == len(columns): break

    for key in columns:
        if len(columns[key]) == 1:
            singleton.add(columns[key][0])
            continue
        for dig in columns[key]: 
            counter = 0
            for others in columns:
                if dig not in columns[others]:
                    counter+=1
            if counter == len(columns)-1:
                columns[key] = [dig]
                singleton.add(dig)
                break
print(columns)

ans = 1
for key in columns:
    if 'departure' not in key: continue
    ans = ans*myTicket[columns[key][0]]

print(errRate)

print(ans)

        
     
     

