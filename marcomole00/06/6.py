check = []
group = []
sum = 0
ao = 0

def checkGroup(group):
    first = group[0]
    print(first)
    if len(group) == 1: return len(first)
    group = group[1:]
    nOfAnswerEverybodyInAGroupAnswered =0
    for ans in first:
        obama = False
        for children in group:
            if ans in children: 
                obama = True
            else: 
                obama = False
                break
        if obama == True:
            print(ans)
            nOfAnswerEverybodyInAGroupAnswered +=1

    return nOfAnswerEverybodyInAGroupAnswered


with open('marcomole00/6/input.txt') as f:
    for line in f:
        if line=='\n':
            sum += len(check)
            check = []
            ao = ao + checkGroup(group)
            #print('ao ', ao)
            group = []
        else:
            line = line.strip('\n')
            group.append(line)
            for char in line:
                if char not in check:
                    check.append(char)


sum += len(check)
ao = ao + checkGroup(group)
#print('ao ', ao) 
 

print(sum)
print(ao)

