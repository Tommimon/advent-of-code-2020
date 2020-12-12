with open('input.txt', 'r') as file:
    totalEast = 0
    totalNorth = 0
    dEast = 10
    dNorth = 1
    for fullLine in file.readlines():
        line = fullLine.strip('\n').replace('R', 'L-').replace('S', 'N-').replace('W', 'E-')
        if line[0] == 'E':
            dEast += int(line[1:])
        elif line[0] == 'N':
            dNorth += int(line[1:])
        elif line[0] == 'L':
            rot = (int(line[1:]) // 90) % 4
            tmp = dEast
            dEast = dEast * ((rot + 1) % 2) * (-rot + 1) + dNorth * (rot % 2) * (rot - 2)
            dNorth = dNorth * ((rot + 1) % 2) * (-rot + 1) + tmp * (rot % 2) * (-rot + 2)
        elif line[0] == 'F':
            totalEast += dEast * int(line[1:])
            totalNorth += dNorth * int(line[1:])
print(abs(totalEast) + abs(totalNorth))
