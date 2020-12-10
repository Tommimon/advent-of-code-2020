counter1 = 0
counter2 = 0
with open('input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    for g in groups:
        counter1 += len(set(g.replace('\n', '')))
        answers = list(map(set, g.split('\n')))
        counter2 += len(answers[0].intersection(*answers))
print(counter1)
print(counter2)
