with open('./Gonduls/24/input.txt') as inputf:
    lines = inputf.read().split('\n')

paths = []
for line in lines:
    paths.append(line.replace('e', 'e ').replace('w', 'w ').split(' '))
    if '' in paths[-1]:
        paths[-1].remove('')

coordinates = []
for line in paths:
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
    coordinates.append(tuple(coords))
tiles = []
for line in coordinates:
    if line in tiles:
        tiles.remove(line)
    else:
        tiles.append(line)


######################################## second part (two options, both take more than 2 min to resolve) #########################
for i in range(100):
    #print(len(tiles))
    max_x = max(list(map(lambda el: abs(el[0]), tiles)))
    max_y = max(list(map(lambda el: abs(el[1]), tiles)))
    new_tiles = []
    for x in range(-max_x -2, max_x + 2):
        for y in range(-max_y -2, max_y + 2):
            if((x+y)%2):
                continue
            adjacent = [(x+2,y), (x-2,y), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
            if (x,y) in tiles:
                if (list(map(lambda el: el in tiles, adjacent)).count(True) in (1,2)):
                    new_tiles.append((x,y))
            else:
                if(list(map(lambda el: el in tiles, adjacent)).count(True) == 2):
                    new_tiles.append((x,y))
    tiles = new_tiles

#for i in range(100):
#    check = set()
#    new_tiles = []
#    for el in tiles:
#        x, y = el
#        adjacent = [(x+2,y), (x-2,y), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
#        for elem in adjacent:
#            check.add(elem)
#        check.add(el)
#    for coord in check:
#        x, y = coord
#        adjacent = [(x+2,y), (x-2,y), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
#        if coord in tiles:
#            if (list(map(lambda el: el in tiles, adjacent)).count(True) in (1,2)):
#                new_tiles.append(coord)
#        else:
#            if(list(map(lambda el: el in tiles, adjacent)).count(True) == 2):
#                new_tiles.append(coord)
#    tiles = new_tiles

print(len(tiles))