lista=[]
with open('./Gonduls/9/input.txt', 'r') as inputf:
    for line in inputf:
        lista.append(int(line))

#calculating number and putting it in resultpart1
for ind in range(25, len(lista)):
    notfound = True
    for eligable in lista[ind-25:ind]:
        if ((lista[ind]-eligable) in lista[ind-25:ind]):
            notfound=False
            break
    if(notfound):
        resultpart1=lista[ind]
        break
#check tommaso's program for a better algorithm
for start in range(len(lista)):
    partial = 0
    notfound = True
    end = start 
    while(notfound):
        partial += lista[end]
        if (partial>resultpart1):
            break
        elif(partial<resultpart1):
            end += 1
        else:
            notfound=False
    if(notfound == False):
        print(max(lista[start:end+1])+min(lista[start:end+1]))
        break