data = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
check=[0]*7
valid_docs=0
with open('marcoparadina/4/input_d4.txt') as f:
    for line in f: 
        if line == '\n':
            if sum(check)==7:
                valid_docs+=1
            check=[0]*7            
        else: 
            replaced=line.replace(':', ' ')
            x=replaced.split()       
            for el in data:
                if el in x:
                    check[data.index(el)]=1

if sum(check)==7:
    valid_docs+=1
# This craps corrects the fact that somehow the last valid passport is not added before 
# exiting the for cycle. Needs a more civilized implementation.

print('First part solution', valid_docs)