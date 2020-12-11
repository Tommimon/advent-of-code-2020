from copy import deepcopy
with open('marcomole00/11/input.txt') as file:
    lines = file.read().split('\n')
    lines = list(map(list, lines))

C = len(lines)
R = len(lines[0])
old = 0

while True:
    cop = deepcopy(lines)
    for y in range(C):  
        for x in range(R):
            occupied = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx == 0 and dy == 0: continue
                    xx = x+dx
                    yy = y+dy
                    while  0<= xx < R and 0<= yy < C :
                        if lines[yy][xx] == '#':
                             occupied +=1
                             break
                        if lines[yy][xx] == 'L': break
                        xx += dx
                        yy += dy
                        #part1
                    """ if  0<= xx < R and 0<= yy < C: 
                        if lines[yy][xx] == '#': 
                            occupied +=1 """
            
            if lines[y][x] == 'L' and occupied == 0: 
                #print('caaoaooa')
                cop[y][x] = '#'
            elif lines[y][x] == '#' and occupied >= 5: #4 for part1, 5 for part2
                cop[y][x] = 'L' 
    
    lines = deepcopy(cop)

    add = 0
    for row in lines:
        for el in row:
            if el == '#': add+=1
    #print(add)
    if add ==15: 
        for row in lines: print(row)
        break
    
    if old == add: 
        break
    else:
        old = add

print(add)

                

         
