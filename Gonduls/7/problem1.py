lista = []
with open('input.txt') as f:
    for line in f:
        lista.append([line.split(' contain')[0][:-1],line.split(' contain')[1][1:].replace('.','').replace('\n','').replace('bags','bag').split(', ')])

counted = ['shiny gold bag']
def recursive_counting(stringa):
    partial_sol=1
    for line in lista:
        for el in line[1]:
            if (stringa in el[2:] and (line[0] not in counted)):
                counted.append(line[0])
                partial_sol= recursive_counting(line[0]) + partial_sol

    return partial_sol


print (recursive_counting('shiny gold bag') - 1)