with open('./Gonduls/13/input.txt', 'r') as inputf:
        lista= list(inputf.read().split('\n'))
        lista[1] = lista[1].split(',')
buses =[]
for elem in lista[1]:
    if (elem != 'x'):
        buses.append(int(elem))

i = 0
notfound= True
while(notfound):
    for elem in buses:
        if ((int(lista[0])+i)%elem == 0):
            notfound = False
            print(i*elem)
            break
    i += 1
