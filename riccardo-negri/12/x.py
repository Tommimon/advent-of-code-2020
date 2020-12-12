#!/usr/bin/env python
# Day 12 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  1533
# Second part answer: 25235
                
# left 90° -->  (x, y) = (y*-1, x*1) --> -1+1
# right 90° --> (x, y) = (y*1, x*-1) --> +1-1

# rotate P about F 
def rotate(P, F, angle):
    temp = [P[0]-F[0], P[1]-F[1]]
    temp = [temp[1] * angle[0], temp[0] * angle[1]]
    return temp[0]+F[0], temp[1]+F[1]

with open('input.txt', 'r') as f:
    acts = f.read().replace('N', '+0+1').replace('E', '+1+0').replace('W', '-1+0').replace('S', '+0-1').replace('L', '-1+1').replace('R', '+1-1').replace('F', '+7+7').split()
    x, y, direction = 0, 0, [1, 0]              # first part
    x_ship, y_ship, x_pt, y_pt = 0, 0, 10, 1    # second part
    for act in acts:
        if int(act[0:2])+int(act[2:4]) == 1 or int(act[0:2])+int(act[2:4]) == -1:
            x, y = x+int(act[0:2])*int(act[4:]), y+int(act[2:4])*int(act[4:])
            x_pt, y_pt = x_pt+int(act[0:2])*int(act[4:]), y_pt+int(act[2:4])*int(act[4:])
        elif int(act[0:2])+int(act[2:4]) == 0:
            for i in range(0, int(int(act[4:])/90)):
                direction = [direction[1] * int(act[0:2]), direction[0] * int(act[2:4])]
                x_pt, y_pt = rotate([x_pt, y_pt], [0, 0], [int(act[0:2]), int(act[2:4])])
        else:
            x, y = x+direction[0]*int(act[4:]), y+direction[1]*int(act[4:])
            x_ship, y_ship = x_ship+x_pt*int(act[4:]), y_ship+y_pt*int(act[4:])
    print("First part answer:  ", abs(x)+abs(y))   
    print("Second part answer: ", abs(x_ship)+abs(y_ship))     