#Pretty painless, just add another dimension in the neighbors search and in the input parse.
#What is painful is runtime

#xyz = str(x)+","+str(y)+","+str(z)             encode
#xyzList = [int(x) for x in xyz.split(',')]     decode

coords = {}
coordsCopy = {}

def findNeighbors(xyzw0):
    neighbors = []
    x0, y0, z0, w0 = [int(x) for x in xyzw0.split(',')]
    for w in range(w0-1, w0+2):
        for z in range(z0-1, z0+2):
            for y in range(y0-1, y0+2):
                for x in range(x0-1, x0+2):
                    neighbors.append(str(x)+","+str(y)+","+str(z)+","+str(w))
    neighbors.remove(xyzw0)
    return neighbors

with open("input.txt") as file:
    lines = file.read().split('\n')
    w = 0
    z = 0
    y = 1
    for line in lines:
        x = -1
        for c in line:
            xyzw = str(x)+","+str(y)+","+str(z)+","+str(w)
            coords[xyzw] = c
            x += 1
        y -= 1

coordsCopy = coords.copy()
for coord in coords:
    neighbors = findNeighbors(coord)
    for n in neighbors:
        if n not in coords:
            coordsCopy[n] = '0'
coords = coordsCopy.copy()

print(coords)

for nSteps in range(6):
    coordsCopy = coords.copy()
    for coord in coords:
        hashcounter = 0
        neighbors = findNeighbors(coord)
        for n in neighbors:
            if n in coords:
                if coords[n] == '#':
                    hashcounter += 1
        if coords[coord] == '#' and (hashcounter < 2 or hashcounter > 3): coordsCopy.update({coord:'.'})
        if (coords[coord] == '.' or coords[coord] == '0') and (hashcounter == 3): coordsCopy.update({coord:'#'})
        elif coords[coord] == '0': coordsCopy.update({coord:'.'})
    coords = coordsCopy.copy()
    for coord in coords:
        neighbors = findNeighbors(coord)
        for n in neighbors:
            if n not in coords:
                coordsCopy[n] = '0'
    coords = coordsCopy.copy()

counter = 0
for coord in coords:
    if coords[coord] == '#': counter += 1
print(counter)