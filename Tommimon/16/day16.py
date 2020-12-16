with open('input.txt', 'r') as file:
    paragraph = file.read().replace('your ticket:', 'nearby tickets:').split('\n\nnearby tickets:\n')
rules = paragraph[0].split('\n')
for i in range(len(rules)):
    prt = rules[i].replace(': ', '-').replace(' or ', '-').split('-')
    rules[i] = {'name': prt[0], 'min1': int(prt[1]), 'max1': int(prt[2]), 'min2': int(prt[3]), 'max2': int(prt[4])}
mine = list(map(int, paragraph[1].split(',')))
nearby = list(map(lambda el: list(map(int, el.split(','))), paragraph[2].split('\n')))
possibilities = list(map(lambda el: [], [None] * len(rules)))
total = 0
for n in nearby.copy():
    invalid = False
    for e in n:
        correct = False
        for r in rules:
            if r['min1'] <= e <= r['max1'] or r['min2'] <= e <= r['max2']:
                correct = True
                break
        if not correct:
            total += e
            invalid = True
    if invalid:
        nearby.remove(n)
print(total)
for r in rules:
    for pos in range(len(rules)):
        correct = True
        for n in nearby:
            if not(r['min1'] <= n[pos] <= r['max1'] or r['min2'] <= n[pos] <= r['max2']):
                correct = False
                break
        if correct:
            possibilities[pos].append(r['name'])
change = True
positions = [None] * len(rules)
while change:
    change = False
    for i, p in enumerate(possibilities):
        if positions[i] is None and len(p) == 1:
            positions[i] = p[0]
            for other in possibilities:
                if p != other:
                    try:
                        other.remove(p[0])
                    except ValueError:
                        pass
            change = True
res = 1
for i, name in enumerate(positions):
    if 'departure' in name:
        res *= mine[i]
print(res)
