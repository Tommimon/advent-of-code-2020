def manhattan(x,y):
    x = abs(x)
    y= abs(y)
    return x +y

compass = ['N','E','S','W']
with open('marcomole00/12/input.txt') as file:
    lines = file.read().split('\n')


waypoint = [10,1]#10 east, 1 north
x= 0
y=0

for line in lines:
    dir = line[:1]
    amount = int(line[1:])
    if dir == 'W':
        dir = 'E'
        amount = -amount
    if dir == 'S':
        dir = 'N'
        amount = -amount
    if dir == 'L': # rotating left by theta is rotating right by 360-theta
        dir ='R'
        amount = 360-amount   
    if dir == 'F':
        x += waypoint[0]*amount
        y+=waypoint[1]*amount
    if dir in compass:
        if dir == 'E': waypoint[0]+= amount
        if dir == 'N': waypoint[1]+= amount
    if dir =='R':
        if amount == 180:
            waypoint[0] = -waypoint[0] 
            waypoint[1] = -waypoint[1] 
        if amount == 90:
            temp = waypoint[0]
            waypoint[0] = waypoint[1] 
            waypoint[1] = -temp 
        if amount == 270:
            temp = waypoint[0]
            waypoint[0] = -waypoint[1] 
            waypoint[1] = temp 
    print('waypoint coord = ', waypoint[0], waypoint[1])
    print('x: ', x, 'y: ', y)

        
print(manhattan(x,y))

