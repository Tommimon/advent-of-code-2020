counter = 0

with open('input.txt', 'r') as file:
    for rowIndex, fullLine in enumerate(file.readlines()):
        line = fullLine[:-1]  # remove ending \n
        if line[(rowIndex * 3) % 31] == '#':
            counter += 1

print(counter)
