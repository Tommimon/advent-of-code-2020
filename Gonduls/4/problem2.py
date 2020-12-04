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
    if (len(element.split(' '))==9 or (len(element.split(' '))==8 and not ('cid' in element))):
        risultato += 1
    i += 1
print (risultato)