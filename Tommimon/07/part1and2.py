def contains(rules, found, color, bags_in):
    global countInGold
    if color == 'shiny gold':
        countInGold += bags_in
    for r in rules:
        for elem in r[1:]:
            if color in elem:
                found.add(r[0])
                contains(rules, found, r[0], bags_in * int(elem.split(' ')[0]))


containGold = set()
countInGold = 0
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' bags contain ', '.').replace(', ', '.').split('.')[:-1]
contains(lines, containGold, 'shiny gold', 0)
print(len(containGold))

for line in lines.copy():
    if line[0] in containGold:
        del lines[lines.index(line)]
countInGold = 0
for rule in lines:
    contains(lines, containGold, rule[0], 1)
print(countInGold - 1)
