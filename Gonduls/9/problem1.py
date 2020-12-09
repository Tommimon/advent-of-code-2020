lista=[]
with open('input.txt', 'r') as inputf:
    for line in inputf:
        lista.append(int(line))

for ind in range(25 , len(lista)):
    notfound = True
    for eligable in lista[ind-25:ind]:
        if ((lista[ind]-eligable) in lista[ind-25:ind]):
            notfound=False
            break
    if(notfound):
        print(lista[ind])
        break