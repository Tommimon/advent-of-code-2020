# i beg you to shoot in my face and public shame my dead body

import copy
with open('marcomole00/11/input.txt') as file:
    lines = file.read().split('\n')
    lines = list(map(list, lines))
    print(len(lines))

old = 0   
while True:
   # cop = copy.deepcopy(lines)
    cop2 = copy.deepcopy(lines)
   # copia = list(map(list, map(tuple, lines)))
    for i in  range(len(lines)):
        for j in range(len(lines[i])):
            seatsFree = 0
            max = 0
            seatsOccupied = [0]*8
            if lines[i][j] == 'L':
                if i>0:
                    max +=1
                    if lines[i-1][j] != '#': 
                        seatsFree += 1
                if i>0 and  j< len(lines[i])-1:
                    max +=1
                    if lines[i-1][j+1] != '#': 
                        seatsFree +=1
                if i>0 and  j>0 :
                    max +=1
                    if lines[i-1][j-1] != '#': 
                        seatsFree += 1
                if j< len(lines[i])-1:
                    max +=1
                    if lines[i][j+1] != '#': 
                        seatsFree += 1
                if j>0:
                    max +=1
                    if lines[i][j-1]!= '#': 
                        seatsFree += 1
                if i < len(lines) -1 :
                    max +=1
                    if lines[i+1][j]!= '#': 
                        seatsFree += 1
                if i < len(lines) -1 and j>0 :
                    max +=1
                    if lines[i+1][j-1] != '#': 
                        seatsFree += 1
                if i < len(lines) -1 and j< len(lines[i]) -1:
                    max +=1
                    if lines[i+1][j+1] != '#': 
                        seatsFree += 1
                if seatsFree == max: 
                    cop2[i][j] = '#'
            
            elif lines[i][j] == '#':
            
                if i>0 and lines[i-1][j] == '#':
                     seatsOccupied[0] = 1
                if i>0 and  j< len(lines[i])-1 and lines[i-1][j+1] == '#': 
                    seatsOccupied[1] = 1
                if i>0 and  j>0 and lines[i-1][j-1] == '#':
                     seatsOccupied[2] = 1
                if j< len(lines[i]) -1 and  lines[i][j+1] == '#': 
                    seatsOccupied[3] = 1
                if j>0 and  lines[i][j-1] == '#': 
                    seatsOccupied[4] = 1
                if i < len(lines)-1 and lines[i+1][j] == '#': 
                    seatsOccupied[5] = 1
                if i < len(lines)-1 and j>0 and lines[i+1][j-1] == '#':
                     seatsOccupied[6] = 1
                if i < len(lines) -1 and j< len(lines[i]) -1 and  lines[i+1][j+1] == '#': 
                    seatsOccupied[7] = 1
    
                if (sum(seatsOccupied)) >= 4: 
                    cop2[i][j] = 'L'
    add = 0
    lines = copy.deepcopy(cop2)
    cop2 = []
    for line in lines: 
        for lett in line: 
            if lett == '#': add += 1
    print(add)
    if old == add: 
        break #why this doesn't work padre pio porco maledetto
    else: old = add   


for row in lines: print(row)
add = 0
for line in lines: 
    for let in line: 
        if let == '#': add+=1
print(add)



        
