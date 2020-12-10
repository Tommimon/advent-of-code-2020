def sequences(numbers, index, sequence, target, counter):
    if sequence[-1] == target:
        return counter + 1
    valid = set(numbers[index+1:index+4]) & set(range(sequence[-1]+1, sequence[-1]+4))
    for v in valid:
        sequence.append(v)
        counter = sequences(numbers, numbers.index(v), sequence, target, counter)
        sequence.pop()
    return counter


with open('input.txt', 'r') as file:
    lines = [0] + sorted(list(map(int, file.read().split('\n'))))
parts = [[]]
for line in range(len(lines)):
    if line != 0 and lines[line] - lines[line - 1] == 3:
        parts.append([])
    parts[-1].append(lines[line])
arrangements = []
for p in parts:
    arrangements.append(sequences(p, 0, [min(p)], max(p), 0))
prod = 1
for c in arrangements:
    prod *= c
print(prod)
