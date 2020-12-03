slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

counters = [0] * 5
for indexSlope, slope in enumerate(slopes):
    with open('input.txt', 'r') as file:
        for rowIndex, fullLine in enumerate(file.readlines()):
            if rowIndex % slope[1] == 0:
                line = fullLine.replace('\n', '')  # remove ending \n
                if line[(rowIndex // slope[1] * slope[0]) % len(line)] == '#':
                    counters[indexSlope] += 1

print(counters[1])
product = 1
for c in counters:
    product *= c
print(product)
