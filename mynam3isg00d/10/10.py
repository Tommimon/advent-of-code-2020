numDict = {}

def check(joltages, elem):
    if elem == max(joltages):
        return 1
    if elem in numDict:
        return numDict[elem]

    if elem+1 in joltages:
        b1 = check(joltages, elem+1)
    else:
        b1 = 0
    if elem+2 in joltages:
        b2 = check(joltages, elem+2)
    else:
        b2 = 0
    if elem+3 in joltages:
        b3 = check(joltages, elem+3)
    else:
        b3 = 0
    numDict[elem] = b1 + b2 + b3
    return numDict[elem]

with open("mynam3isg00d/10/input.txt") as file:
    #tommaso culo
    joltages = file.read().split('\n')
    joltages = sorted(list(map(int, joltages))+[0])
    joltages2 = joltages[1:]+[max(joltages)+3]
    joltages3 = [x1 - x2 for (x1, x2) in zip(joltages2, joltages)]
    print("Part 1: " + str(joltages3.count(1) * joltages3.count(3)))
    print("Part 2: " + str(check(joltages, 0)))