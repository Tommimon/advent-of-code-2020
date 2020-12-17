from itertools import permutations as combos
with open('input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')

close_points = set(combos([0,0,0,1,1,1,-1,-1,-1],3)).remove((0,0,0))
def return_close(x, y, z):
    answer = []
    for point in close_points:
        answer.append((x+point[0], y+point[1], z+point[2]))
    return answer


pocket_dimension = {}
for y, line in enumerate(lista):
    for x, char in enumerate(line):
        pocket_dimension[x,y,0]=char
for el in pocket_dimension:
    print(el, ': ',pocket_dimension[el])

