

with open('marcomole00/11/test') as file:
    lines = file.read().split('\n')
    lines = list(map(list, lines))
    cop = []
    old = 0

    
while True:
    #print('ciao')
    copia = list(map(list, map(tuple, lines)))
    for i in  range(len(lines)):
    
        for j in range(len(lines[i])):
            seatsOccupied = [0]*8 
            if lines[i][j] == '.': break
            if lines[i][j] == 'L':
                try:
                    if lines[i-1][j] != '#': seatsOccupied[0] = 0
                except IndexError: pass
                try:
                    if lines[i-1][j+1] != '#': seatsOccupied[1] = 0
                except IndexError: pass

                try:
                    if lines[i-1][j-1] != '#': seatsOccupied[2] = 0
                except IndexError: pass
                try:
                    if lines[i][j+1] != '#': seatsOccupied[3] = 0
                except IndexError: pass
                try:
                    if lines[i][j-1]!= '#': seatsOccupied[4] = 0
                except IndexError: pass
                try:
                    if lines[i+1][j]!= '#': seatsOccupied[5] = 0
                except IndexError: pass
                try:
                    if lines[i+1][j-1] != '#': seatsOccupied[6] = 0
                except IndexError: pass
                try:
                    if lines[i+1][j+1] != '#': seatsOccupied[7] = 0
                except IndexError: pass
                if (sum(seatsOccupied)) == 0: 
                    lines[i][j] = '#'
            
            elif lines[i][j] == '#':
                try:
                    if lines[i-1][j] == '#': seatsOccupied[0] = 1
                except IndexError: pass
                try:
                    if lines[i-1][j+1] == '#': seatsOccupied[1] = 1
                except IndexError: pass

                try:
                    if lines[i-1][j-1] == '#': seatsOccupied[2] = 1
                except IndexError: pass
                try:
                    if lines[i][j+1] == '#': seatsOccupied[3] = 1
                except IndexError: pass
                try:
                    if lines[i][j-1] == '#': seatsOccupied[4] = 1
                except IndexError: pass
                try:
                    if lines[i+1][j] == '#': seatsOccupied[5] = 1
                except IndexError: pass
                try:
                    if lines[i+1][j-1] == '#': seatsOccupied[6] = 1
                except IndexError: pass
                try:
                    if lines[i+1][j+1] == '#': seatsOccupied[7] = 1
                except IndexError: pass
                if (sum(seatsOccupied)) >= 4: 
                    lines[i][j] = 'L'
    add = 0
    for line in lines: 
        for let in line: 
            if let == '#': add+=1
    if old == add: break #why this doesn't work padre pio porco maledetto
    else: old = add 


print(add)



        
