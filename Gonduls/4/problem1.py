with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()

lista = ['']
for element in inlist:
    if (element == '\n'):
        lista.append('')
        continue
    lista[-1]=lista[-1]+element[:-1]+' '

risultato=0
i=0
for element in lista:
    lista[i]=element.split(' ')[:-1]
    if (len(lista[i])==8 or (len(lista[i])==7 and not ('cid' in element))):
        risultato += 1
    i += 1
print (risultato)