lista = []
with open('input.txt') as f:
    for line in f:
        lista.append([line.split(' contain')[0][:-1],line.split(' contain')[1][1:].replace('.','').replace('\n','').replace('bags','bag').split(', ')])

def recursive_counting(stringa):
    partial_sol=1
    if(stringa == 'shiny gold bag'):
        partial_sol=0   #shiny gold bag doesn't count as a solution
    for line in lista:
        if (line[0] == stringa):
            if(line[1][0] == 'no other bag'):
                return 1
            for el in line[1]:
                partial_sol = int(el[0]) * recursive_counting(el[2:]) + partial_sol
            break
    return partial_sol

print (recursive_counting('shiny gold bag'))