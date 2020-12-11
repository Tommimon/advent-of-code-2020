#Could EASILY be joined with part 1, that is if i wasn't lazy

import copy

directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

def checkNeighbors2(x, y):
    neighbors = []
    notFound = True
    for d in directions:
        notFound = True
        i = x
        j = y
        while (i >= 0 and i < len(grid[0]) and j >= 0 and j < len(grid)):
            debug = grid[j][i]
            if(grid[j][i] == '#' and (i!=x or j!=y)):
                neighbors.append('#')
                notFound = False
                break
            if(grid[j][i] == 'L' and (i!=x or j!=y)): break
            i += d[0]
            j += d[1]
        if(notFound):
            neighbors.append('L')
    return neighbors

counter = 0
with open("mynam3isg00d/11/input.txt") as file:
    grid = file.read().split('\n')
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    while True:
        gridNew = copy.deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                neighbors = checkNeighbors2(x, y)
                if (grid[y][x] == 'L') and (neighbors.count('#') == 0): gridNew[y][x] = '#'
                if (grid[y][x] == '#') and (neighbors.count('#') >= 5): gridNew[y][x] = 'L'
        if gridNew == grid:
            break
        grid = copy.deepcopy(gridNew)
for row in grid:
    counter += row.count('#')
print("Part 2: " + str(counter))