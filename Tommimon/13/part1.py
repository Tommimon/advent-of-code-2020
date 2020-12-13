with open('input.txt', 'r') as file:
    time = int(file.readline())
    ids = file.readline().split(',')
minimum = time
idMin = 0
for i in ids:
    if i != 'x' and int(i) - time % int(i) < minimum:
        minimum = int(i) - time % int(i)
        idMin = int(i)
print(idMin * minimum)
