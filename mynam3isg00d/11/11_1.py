#Part 1, i thought i was gonna join them thats why the long ass function but eewwwwww optimisation :ssss

def checkNeighbors1(x, y):
    #I break Tommaso's record for longest oneliner
    return [grid[i][j] if  i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) else 0 for j in range(x-1, x+2) for i in range(y-1, y+2)]


import copy
counter = 0
with open("mynam3isg00d/11/input.txt") as file:
    grid = file.read().split('\n')
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    while True:
        gridNew = copy.deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                neighbors = checkNeighbors1(x, y)
                del neighbors[4]
                if (grid[y][x] == 'L') and (neighbors.count('#') == 0): gridNew[y][x] = '#'
                if (grid[y][x] == '#') and (neighbors.count('#') >= 4): gridNew[y][x] = 'L'
        if gridNew == grid:
            break
        grid = copy.deepcopy(gridNew)
for row in grid:
    counter += row.count('#')
print("Part 1: " + str(counter))