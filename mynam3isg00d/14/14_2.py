from itertools import *

mem = {}

def updateMemory(mask, memAss):
    for inst in memAss:
        pos, value = inst.split(' = ')
        posB = list(str(bin(int(pos)))[2:])
        #places X in good spots :)
        base = int(mask.replace('X','0'), 2)
        mask = list(mask)
        posB = ['0']*(36-len(posB)) + posB
        for i in range(36):
            if mask[i] == 'X': posB[i] = 'X'
            if mask[i] == '1': posB[i] = '1'
        posB = ''.join(posB)

        #find base value
        base = int(posB.replace('X', '0'), 2)

        #create list of partial values
        partialValues = []
        for i in range(36):
            if posB[i] == 'X':
                partialValues.append(2**(35-i))
        dim = len(partialValues)
        partialValues += [0]*(len(partialValues))

        #find possible permutetions and add them to set of possible sums
        sums = set()
        comb = combinations(partialValues, dim)
        for i in comb:
            sums.add(sum(i))

        #put value in every mem slot
        for s in sums:
            mem[base+s] = int(value)
        
        mask = ''.join(mask)

with open("input.txt") as file:
    infos = file.read().replace('mask = ','\n').strip('\n').replace('mem[','').replace(']','').split('\n\n')
    for info in infos:
        lines = info.split('\n')
        mask = lines[0]
        memAss = lines[1:]
        updateMemory(mask, memAss)
print("Part 2: " + str(sum(mem.values())))