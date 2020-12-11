grid = []
with open('input.txt', 'r') as file:
    for fullLine in file.readlines():
        grid.append([9])
        for char in fullLine.replace('\n', ''):
            if char == '.':
                grid[-1].append(9)
            else:
                grid[-1].append(char)
        grid[-1].append(9)
grid.append([9] * len(grid[0]))
grid.insert(0, [9] * len(grid[0]))
adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(1, len(grid[:-1])):
    for j in range(1, len(grid[i][:-1])):
        if isinstance(grid[i][j], str):
            grid[i][j] = 0
            for delta in adjacent:
                elem = grid[i + delta[0]][j + delta[1]]
                if (isinstance(elem, int) and elem < 9) or elem == 'L':
                    grid[i][j] += 1
changed = True
while changed:
    changed = False
    for i in range(1, len(grid[:-1])):
        for j in range(1, len(grid[i][:-1])):
            if grid[i][j] < 4:
                for delta in adjacent:
                    elem = grid[i + delta[0]][j + delta[1]]
                    if 4 <= elem < 9:
                        changed = True
                        grid[i + delta[0]][j + delta[1]] = 10
    for i in range(1, len(grid[:-1])):
        for j in range(1, len(grid[i][:-1])):
            if grid[i][j] == 10:
                for delta in adjacent:
                    if grid[i + delta[0]][j + delta[1]] < 9:
                        grid[i + delta[0]][j + delta[1]] -= 1
                grid[i][j] = 9
#for i in grid:
#    print(list(map(str, i)))
#print('\n\n\n')
counter = 0
for row in grid:
    for i in row:
        if i < 9:
            counter += 1
print(counter)
