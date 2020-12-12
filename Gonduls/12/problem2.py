with open('input.txt', 'r') as inputf:
        lista= list(inputf.read().split('\n'))
cardinals = ['N','E','S','W','N','E','S','W']
directions = {'N':[1,0],'E':[0,1],'S':[-1,0],'W':[0,-1]}
position = [0,0]
waypoint = [[1,'N'],[10,'E']]
for line in lista:
    if (line[0] in directions.keys()):
        waypoint = [[waypoint[0][0] + directions[line[0]][0]*int(line[1:]), 'N'] , [waypoint[1][0] + directions[line[0]][1]*int(line[1:]), 'E']]
        if(waypoint[0][0]<0):
            waypoint[0][1]='S'
        if(waypoint[1][0]<0):
            waypoint[1][1]='W'
    if (line[0] == 'R'):
        waypoint = [[waypoint[0][0], cardinals[cardinals.index(waypoint[0][1]) + int(int(line[1:])/90)]] , [waypoint[1][0], cardinals[cardinals.index(waypoint[1][1]) + int(int(line[1:])/90)]]]
    if (line[0] == 'L'):
        waypoint = [[waypoint[0][0], cardinals[cardinals.index(waypoint[0][1]) - int(int(line[1:])/90)]] , [waypoint[1][0], cardinals[cardinals.index(waypoint[1][1]) - int(int(line[1:])/90)]]]
    if(waypoint[0][1] == 'E' or waypoint[0][1] == 'W'):
        waypoint = [waypoint[1],waypoint[0]]
    for ind, way in enumerate(waypoint):
        waypoint[ind][0]= abs(waypoint[ind][0]) * directions[way[1]][ind]
    if (line[0] == 'F'):
        position = [position[0] + waypoint[0][0]*int(line[1:]) , position[1] + waypoint[1][0]*int(line[1:])]

print(abs(position[0])+abs(position[1]))