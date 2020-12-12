with open('input.txt', 'r') as file:
    dirs = ['E', 'N', 'E-', 'N-']
    index = 0
    east = 0
    north = 0
    for fullLine in file.readlines():
        line = fullLine.strip('\n').replace('R', 'L-').replace('S', 'N-').replace('W', 'E-').replace('F', dirs[index])
        if line[0] == 'E':
            east += int(line[1:])
        elif line[0] == 'N':
            north += int(line[1:])
        elif line[0] == 'L':
            index = (index + int(line[1:])//90) % 4
print(abs(east) + abs(north))
