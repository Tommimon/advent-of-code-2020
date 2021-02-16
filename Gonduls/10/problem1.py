with open('./Gonduls/10/input.txt', 'r') as inputf:
        lista= list(map(int, inputf.read().split('\n')))
lista.append(0)
lista=sorted(lista)
lista.append(lista[-1]+3)
diff_one = 0
diff_three = 0
for i, num in enumerate(lista[:-1]):
    if (lista[i+1] == num + 3):
        diff_three +=1
    elif (lista[i+1] == num + 1):
        diff_one +=1
print(diff_one*diff_three)