def removeEx(lista,char):
    for el in lista:
        if el != char: lista.remove(el)
    return lista

with open('marcomole00/11/input.txt') as file:
    lines = file.read().split('\n')
    lines = list(map(list, lines))
    cop = lines.copy()
    first = True
    
while True:
    print('ciao')
    cop = lines.copy()
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
                    change = True
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
                    print(lines[i][j], '  ', print(cop[i][j]))
    if lines == cop: break
add = 0

for line in lines: 
    for let in line: 
        if let == '#': add+=1
   
print(add)
        
