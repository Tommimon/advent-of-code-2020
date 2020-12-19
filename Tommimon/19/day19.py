def match(string, rule):
    global rules_list
    if len(rule) == 0:  # if no rule always match
        return {0}  # with this I sum 0 and I keep the previous lengths
    elif len(string) == 0:  # never match
        return set()
    elif isinstance(rule[0], str):
        if string[0] == rule[0]:
            return {1}
    elif -1 in rule:
        separator = rule.index(-1)
        return match(string, rule[:separator]).union(match(string, rule[separator+1:]))
    else:
        possible = set()
        l1 = match(string, rules_list[rule[0]])
        for i in l1:
            l2 = match(string[i:], rule[1:])
            for j in l2:
                possible.add(i + j)
        return possible
    return set()  # if rule is string but different


with open('input.txt', 'r') as file:
    paragraph = file.read().split('\n\n')
rules_list = []
for r in paragraph[0].split('\n'):
    parts = r.replace(':', '').replace('|', '-1').replace('"', '').split(' ')
    index = int(parts[0])
    rules_list += [None] * (index - len(rules_list) + 1)  # resize list to reach new index
    try:
        rules_list[index] = list(map(int, parts[1:]))
    except ValueError:
        rules_list[index] = [parts[1]]  # if is "a" or "b"

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
