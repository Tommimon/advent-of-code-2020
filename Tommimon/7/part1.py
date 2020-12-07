def contains(rules, found, color):
    for r in rules:
        for elem in r[1:]:
            if color in elem:
                found.add(r[0])
                contains(rules, found, r[0])


containGold = set()
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' bags contain ', '.').replace(', ', '.').split('.')[:-1]
contains(lines, containGold, 'shiny gold')
print(len(containGold))
