# check Tommimon' solution to first part for a better/easier/faster/shorter algorithm
with open('./Gonduls/24/input.txt') as inputf:
    lines = inputf.read().split('\n')

paths = []
for line in lines:
    paths.append(line.replace('e', 'e ').replace('w', 'w ').split(' '))
    if '' in paths[-1]:
        paths[-1].remove('')

coordinates = []
for line in paths:
    print(line)
    print('e:',line.count('e'), ' w:',line.count('w'), ' ne:',line.count('ne'), ' se:',line.count('se'), ' nw:',line.count('nw'), ' sw:',line.count('sw'))
    coords = [0,0]
    for el in line:
        if el == 'e':
            coords[0] += 2
        if el == 'w':
            coords[0] -= 2
        if el == 'ne':
            coords[0] += 1
            coords[1] += 1
        if el == 'se':
            coords[0] += 1
            coords[1] -= 1
        if el == 'nw':
            coords[0] -= 1
            coords[1] += 1
        if el == 'sw':
            coords[0] -= 1
            coords[1] -= 1
    coordinates.append(coords)
answer = []
for line in coordinates:
    if line in answer:
        answer.remove(line)
    else:
        answer.append(line)

print(len(answer))