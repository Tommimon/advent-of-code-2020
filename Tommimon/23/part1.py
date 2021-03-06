def move(cups, turns):
    size = len(cups)
    for i in range(turns):
        picked = cups[:3]
        cups = cups[3:]
        dest = (cups[len(cups) - 1] - 2) % size + 1
        while dest in picked:
            dest = (dest - 2) % size + 1
        index = cups.index(dest) + 1
        cups[index:index] = picked
        cups.append(cups.pop(0))  # change current
    return cups


puzzleInput = '487912365'

cupsList = list(map(int, puzzleInput))
cupsList.append(cupsList.pop(0))  # move everything forward of one because for me last element is current
cupsList = move(cupsList, 100)
print(''.join(''.join(map(str, cupsList)).split('1')[::-1]))
