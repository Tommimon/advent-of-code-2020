with open('input.txt', 'r') as inputf:
        lista= list(inputf.read().split('\n'))
cardinals = ['N','E','S','W','N','E','S','W']
directions = {'N':[1,0],'E':[0,1],'S':[-1,0],'W':[0,-1]}
position = [[0,0],'E']
for line in lista:
    if (line[0] in directions.keys()):
        position = [[position[0][0] + directions[line[0]][0]*int(line[1:]),position[0][1] + directions[line[0]][1]*int(line[1:])], position[1]]
    if (line[0] == 'R'):
        position[1] = cardinals[cardinals.index(position[1]) + int(int(line[1:])/90)]
    if (line[0] == 'L'):
        position[1] = cardinals[cardinals.index(position[1]) - int(int(line[1:])/90)]
    if (line[0] == 'F'):
        position = [[position[0][0] + directions[position[1]][0]*int(line[1:]),position[0][1] + directions[position[1]][1]*int(line[1:])], position[1]]
    #print(position[0][0], ' ', position[0][1], ' ', position[1])
print(abs(position[0][0])+abs(position[0][1]))