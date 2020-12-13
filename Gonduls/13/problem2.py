with open('input.txt', 'r') as inputf:
        lista= list(inputf.read().split('\n'))
        lista[1] = lista[1].split(',')
buses =[]
for i, elem in enumerate(lista[1]):
    if (elem != 'x'):
        buses.append([int(elem), i, True])
times = 0
step = 1
i = 0
notfound= True
while(notfound):
    if all(map(lambda el: el==0, map(lambda ele: (i+ele[1])%ele[0], buses))):
        break
    for bus in buses:
        if (bus[2] and (i+bus[1])%bus[0]==0):
            bus[2] = False
            step *= bus[0]
    i += step
print(i)