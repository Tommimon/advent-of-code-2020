from itertools import permutations as combos
with open('./Gonduls/17/input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')

close_points = list(set(combos([0,0,0,0,1,1,1,1,-1,-1,-1,-1],4)))
close_points.remove((0,0,0,0))

def return_close(position):
    answer = []
    for point in close_points:
        answer.append((position[0]+point[0], position[1]+point[1], position[2]+point[2], position[3]+point[3]))
    return answer

def new_diz(old):
    #have to add outer layer of points close to old points to not repeat operation of creating new list twice
    momentary = []
    for el in old:
        momentary += return_close(el)
    for point in set(momentary):
        if (point not in old.keys()):
            old[point]='.'
    #creating new list of points
    new = {}
    for el in old:
        close = return_close(el)
        active = 0
        for point in close:
            if (point in old.keys() and old[point]=='#'):
                active += 1
        if (active == 3 or (active == 2 and old[el]=='#')):
            new[el] = '#'
        else:
            new[el] = '.'
    return new

pocket_dimension = {}
for y, line in enumerate(lista):
    for x, char in enumerate(line):
        pocket_dimension[x,y,0,0]=char

for i in range(6):
    pocket_dimension = new_diz(pocket_dimension)

print(list(pocket_dimension.values()).count('#'))
#differences with problem1: 4th dimension added, nothing new apart from that