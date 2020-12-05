with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    lines.remove('')
    for i in range(len(lines)):
        lines[i] = lines[i].replace('F', 'L').replace('L', '0')
        lines[i] = lines[i].replace('B', 'R').replace('R', '1')
        lines[i] = int(lines[i], 2)
    print(max(lines))
