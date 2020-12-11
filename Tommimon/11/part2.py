# 9 is '.'
# 10 is forever empty 'L'
# 11 is jut found empty 'L'
grid = []
with open('input.txt', 'r') as file:
    for fullLine in file.readlines():
        grid.append([])
        for char in fullLine.replace('\n', ''):
            if char == '.':
                grid[-1].append(9)
            else:
                grid[-1].append(char)
adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if isinstance(grid[i][j], str):
            grid[i][j] = 0
            for delta in adjacent:
                m = 1
                while 0 <= i + delta[0]*m < len(grid) and 0 <= j + delta[1]*m < len(grid[0]):
                    elem = grid[i + delta[0]*m][j + delta[1]*m]
                    if not (isinstance(elem, int) and elem == 9):
                        grid[i][j] += 1  # can be only seat
                        break
                    m += 1
changed = True
while changed:
    changed = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < 5:
                for delta in adjacent:
                    m = 1
                    while 0 <= i + delta[0] * m < len(grid) and 0 <= j + delta[1] * m < len(grid[0]):
                        elem = grid[i + delta[0] * m][j + delta[1] * m]
                        if 5 <= elem != 9:
                            if elem < 10:
                                changed = True
                                grid[i + delta[0] * m][j + delta[1] * m] = 11
                            break
                        m += 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 11:
                for delta in adjacent:
                    m = 1
                    while 0 <= i + delta[0] * m < len(grid) and 0 <= j + delta[1] * m < len(grid[0]):
                        elem = grid[i + delta[0] * m][j + delta[1] * m]
                        if elem != 9:
                            if elem < 10:
                                grid[i + delta[0] * m][j + delta[1] * m] -= 1  # can be only seat
                            break
                        m += 1
                grid[i][j] = 10
counter = 0
for row in grid:
    for i in row:
        if i < 9:
            counter += 1
print(counter)
