#removed a little bit of spaghetti code


def manhattan(x,y):
    x = abs(x)
    y= abs(y)
    return x +y

newCompass = {}
newCompass['E'] = 0
newCompass['W'] = 0
newCompass['S'] = 0
newCompass['N'] = 0

compass = ['N','E','S','W']
with open('marcomole00/12/input.txt') as file:
    lines = file.read().replace('L', 'R-').split('\n')
facing = compass[1]
indexFacing = 1
notDir = ('F', 'L','R')
for line in lines:
    dir = line[:1]
    amount = int(line[1:])
    
    if  dir not in notDir:
        newCompass[dir] += amount
    if dir == 'F':
        newCompass[facing] += amount
    if dir == 'R':
        amount = int(amount/90)
        indexFacing += amount
        indexFacing = indexFacing % 4
        facing = compass[indexFacing]
       
print(newCompass)
x = newCompass['E'] - newCompass['W']
y = newCompass['N'] - newCompass['S']
print('x', x, 'y', y)
print(manhattan(x,y))
