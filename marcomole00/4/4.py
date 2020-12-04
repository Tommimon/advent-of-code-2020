#girls, boys, this is the reason you want to learn regex
#also thanks to marcoparadina to whom i've stolen half the code because i'm rusty with python rn

fields=['byr','iyr','eyr','hgt','hcl','ecl','pid']
eyeColors = ['amb','blu', 'brn', 'gry', 'grn', 'hzl','oth']
fieldCheck=[0]*7
valueCheck=[0]*7
nOfPassports=0
nOfPassportsLimitations = 0
def isValid(field, value):
    if field =='byr' and value.isdecimal and(1920 <= int(value) <= 2002):
        return 1
    if field == 'iyr' and (2010 <= int(value) <= 2020):
        return 1
    if field== 'eyr' and  (2020 <= int(value) <= 2030):
        return 1
    if field =='hgt':
        scale = value[-2:]
        if (scale == 'cm' and  150<=int(value[:-2])<=193) or (scale == 'in' and  59<=int(value[:-2])<=76):
            return 1
    if field =='hcl' and value[0] == '#' and len(value) == 7:
        #print(value)        
        if int(value[1:], 16) <= pow(16,6):
            #print (int(value[1:], 16))
            return 1
    if field =='ecl' and (value in eyeColors):
        return 1
    if field == 'pid' and value.isdecimal() and len(value) == 9:
        if (int(value) <= 999999999):
            return 1 
    
    return 0


with open('marcomole00/4/input.txt') as f:
    for line in f:
        if line == '\n':
            if sum(fieldCheck) == 7: 
                nOfPassports +=1
                if sum(valueCheck) == 7:
                    nOfPassportsLimitations += 1

            
            fieldCheck=[0]*7  
            valueCheck=[0]*7
    
        else:
            line = line.replace(':',' ')
            line = line.split(' ')
            for field in fields:
                if field in line:
                    fieldCheck[fields.index(field)] = 1
                    value = line[line.index(field)+1].strip('\n')
                    valueCheck[fields.index(field)] = isValid(field,value)
                   # print(field + ' value : ' + value + ' is valid ? ' + str(isValid(field,value)))


if sum(fieldCheck) == 7:
     nOfPassports+=1 #in case the last passport in the list is valid 
if sum(valueCheck) == 7:
     nOfPassportsLimitations += 1
print(nOfPassports) 
print(nOfPassportsLimitations)
            
