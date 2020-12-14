#THIS IS NOT HOW YOU CODE, THIS IS NOT GOOD, THIS IS BAD

from copy import deepcopy
import itertools 
with open('marcomole00/14/input.txt') as file:
    lines = file.read().split('\n')

getbin  =  lambda memAddress, n: format(memAddress, 'b').zfill(n)

def applyMaskValue(memValue, mask):
    memValue = bin(memValue).replace('0b', '')[::-1]
    count = 0
    ans = [0]*36
    for dig in memValue:
        ans[35-count] = int(dig)
        count +=1

    for i in range(len(mask)):
        if mask[i] == '1':
            ans[i] = 1
        elif mask[i] == '0': ans[i] = 0
    ans = str(ans).replace('[','').replace(']','').replace(', ','')
    #print(ans)
    return int(str(ans),2)

def applyMaskAddress(memAddress,mask):
    n = 36
    ans = [0]*36
    memAddress = getbin (memAddress,n)
    for i in range(len(mask)):
        if mask[i] == '1': ans[i] = 1
        elif mask[i] == 'X': ans[i] = 'X'
        else: ans[i] = memAddress[i]
    
    return ans

def getSums(lista):
    ans = set()
    zeros = [0]*len(lista)
    temp = itertools.combinations(lista+zeros, len(lista))
    for a in temp: 
        a = list(a)
        ans.add(sum(a))
    return ans

memory =  {}
indexes = []
sums = []
for line in lines:
    
    if line[:4] == 'mask':
        mask = line[7:]
    else:
        line = line.replace(' = ', '.').replace('mem[', '').replace(']', '').split('.')
        memAddress = int(line[0])
        
        memValue = int(line[1])
        #memory[memAddress] = applyMaskValue(memValue, mask) part1
        afterMask = applyMaskAddress(memAddress,mask)
        indexes = []
        sums= []
        for dig in range(len(afterMask)):
            if afterMask[dig] == 'X': indexes.append(35-dig)
        afterMask = str(afterMask).replace('[','').replace(']','').replace(', ','').replace('\'', '').replace('X','0')
        afterMask = int(afterMask,2)
        for el in range(len(indexes)):
            indexes[el] = 2**indexes[el]
        indexes.append(0)
        
        sums = getSums(indexes)
        
        for increment in sums:
            memory[afterMask+increment] = memValue

ans = 0
for key in memory:
    ans += memory[key]
print(ans) 