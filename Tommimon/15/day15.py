# Wait it's all brute force
# Always has been
first = [0, 14, 1, 3, 7, 9]
for length in [2020, 30000000]:
    turns = dict()
    for i in range(1, length + 1):
        if i - 1 < len(first):
            curr = first[i - 1]
        else:
            curr = succ
        if curr in turns:
            succ = i - turns[curr]
        else:
            succ = 0
        turns[curr] = i
    print(curr)
