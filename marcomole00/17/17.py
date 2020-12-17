from copy import deepcopy
with open('marcomole00/17/input.txt') as file:
    lines = file.read().split('\n')
space = {}
""" space = {    #(x,y,z)
    (0,1,0) : '#',
    (1,0,0) : '#',
    (-1,-1,0) : '#',
    (0,-1,0) : '#',
    (1,-1,0) : '#'
} """
print(lines)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        space[(i,j,0)] = lines[i][j]
#spaceCopy = deepcopy(space)
""" for key in spaceCopy:
    (x,y,z) = key
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            for dz in (-1,0,1):
                if (x+dx,y+dy,z+dz) not in spaceCopy: 
                    space[(x+dx,y+dy,z+dz)] = '.' """



for i in range(6):
    spaceCopy = deepcopy(space)
    for key in spaceCopy:
        (x,y,z) = key
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    if (x+dx,y+dy,z+dz) not in spaceCopy: 
                        space[(x+dx,y+dy,z+dz)] = '.'
    
    spaceCopy = deepcopy(space)
    
    #populate the neighbors
    for key in spaceCopy:
        (x,y,z) = key
        
        active = 0
        inactive = 0
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    if dx == dy == dz == 0: continue
                    try:
                        if spaceCopy[(x+dx,y+dy,z+dz)] == '#': active +=1
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


                


