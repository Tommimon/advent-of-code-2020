spoken = {}
num = 1

with open("input.txt") as file:
    inp = file.read().split(',')
    for i in inp:
        spoken[int(i)] = num
        num += 1
last = 0
while num < 30000000:
    if num == 2020:
        print("Part 1: " + str(last))
    if last in spoken:
        t = last
        last = num - spoken[last]
        spoken.update({t: num})
    else:
        spoken[last] = num
        last = 0
    num += 1
print("Oh you're still awake, here's part 2: " + str(last))