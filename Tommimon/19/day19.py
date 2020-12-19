def match(string, rule):
    global rules_list
    if len(string) == 0:
        return set()
    elif len(rule) == 1:
        if isinstance(rule[0], str):
            if string[0] == rule[0]:
                return {1}
            else:
                return set()
        else:
            return match(string, rules_list[rule[0]])
    elif -1 in rule:
        separator = rule.index(-1)
        return match(string, rule[:separator]).union(match(string, rule[separator+1:]))
    elif len(rule) == 2:
        l1 = match(string, rules_list[rule[0]])
        possible = set()
        for i in l1:
            l2 = match(string[i:], rules_list[rule[1]])
            for j in l2:
                possible.add(i + j)
        return possible
    elif len(rule) == 3:
        l1 = match(string, rules_list[rule[0]])
        possible = set()
        for i in l1:
            l2 = match(string[i:], rules_list[rule[1]])
            for j in l2:
                l3 = match(string[i+j:], rules_list[rule[2]])
                for k in l3:
                    possible.add(i + j + k)
        return possible


with open('input.txt', 'r') as file:
    paragraph = file.read().split('\n\n')
rules_list = []
for r in paragraph[0].split('\n'):
    parts = r.replace(':', '').replace('|', '-1').replace('"', '').split(' ')
    index = int(parts[0])
    rules_list += [None] * (index - len(rules_list) + 1)
    try:
        rules_list[index] = list(map(int, parts[1:]))
    except ValueError:
        rules_list[index] = [parts[1]]

counter = 0
for m in paragraph[1].split('\n'):
    if len(m) in match(m, rules_list[0]):
        counter += 1
print(counter)

rules_list[8] = [42, -1, 42, 8]
rules_list[11] = [42, 31, -1, 42, 11, 31]
counter = 0
for m in paragraph[1].split('\n'):
    if len(m) in match(m, rules_list[0]):
        counter += 1
print(counter)
