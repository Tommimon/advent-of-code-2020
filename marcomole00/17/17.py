from copy import deepcopy
with open('marcomole00/17/input.txt') as file:
    lines = file.read().split('\n')
space = {}
#for part1 just delete all mentions of w and dw
for i in range(len(lines)):
    for j in range(len(lines[0])):
        space[(i,j,0,0)] = lines[i][j]

for i in range(6):
    spaceCopy = deepcopy(space)
    for key in spaceCopy:
        (x,y,z,w) = key
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    for dw in (-1,0,1):
                        if (x+dx,y+dy,z+dz,w+dw) not in spaceCopy: 
                            space[(x+dx,y+dy,z+dz,w+dw)] = '.'
    
    spaceCopy = deepcopy(space)
    
    #populate the neighbors
    for key in spaceCopy:
        (x,y,z,w) = key
        
        active = 0
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    for dw in (-1,0,1):
                        if dx == dy == dz == dw == 0: continue
                        try:
                            if spaceCopy[(x+dx,y+dy,z+dz,w+dw)] == '#': active +=1
                        except KeyError: pass

        if spaceCopy[key] == '#': 
            if active != 2 and active !=3:
                space[key] = '.'
        elif spaceCopy[key] == '.':
            if active == 3: space[key] = '#'

counter = 0
for key in space:
    if space[key] == '#':  
        counter+=1

print(counter)


                


