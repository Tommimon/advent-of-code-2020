def sub_many(current, other):
    res_set = set()
    for address in current:
        res_set = res_set.union(set(sub_one(address, other)))
    return res_set


def sub_one(a, other):
    res_list = []
    res_pattern = []
    for j in range(len(a)):
        if a[j] != 'X':
            if other[j] != 'X' and a[j] != other[j]:
                return [a]
            else:
                res_pattern += [a[j]]
        else:
            if other[j] == 'X':
                res_pattern += ['X']
            elif other[j] == '0':
                res_pattern += ['U']
            elif other[j] == '1':
                res_pattern += ['Z']
    for j, c in enumerate(res_pattern):
        if c == 'Z':
            res_pattern[j] = '0'
            res_list.append("".join(res_pattern).replace('Z', 'X').replace('U', 'X'))
            res_pattern[j] = '1'
        elif c == 'U':
            res_pattern[j] = '1'
            res_list.append("".join(res_pattern).replace('Z', 'X').replace('U', 'X'))
            res_pattern[j] = '0'
    return res_list


with open('input.txt', 'r') as file:
    mask = ""
    istructions = []
    for fullLine in file.readlines():
        command = fullLine.strip('\n').replace(']', '').replace('[', ' = ').split(' = ')
        if command[0] == 'mask':
            mask = command[1]
        elif command[0] == 'mem':
            pos = bin(int(command[1]))[2:]
            changedPos = ""
            for i in range(0, len(mask)):
                if mask[len(mask) - 1 - i] == '0':
                    if i < len(pos):
                        changedPos += pos[len(pos) - 1 - i]
                    else:
                        changedPos += '0'
                else:
                    changedPos += mask[len(mask) - 1 - i]
            istructions.append({'addr': changedPos[::-1], 'val': int(command[2])})
total = 0
for revIndex, istr in enumerate(istructions[::-1]):
    addresses = {istr['addr']}
    for otherIstr in istructions[len(istructions)-revIndex:]:  # check only instructions after current
        addresses = sub_many(addresses, otherIstr['addr'])
    count = 0
    for addr in addresses:
        count += 2 ** (addr.count('X'))
    total += count * istr['val']
print(total)
