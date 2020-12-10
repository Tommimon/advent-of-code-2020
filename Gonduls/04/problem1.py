with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()
#would need a space (' ') on last line, not bothering 'cause it works. To be added otherwise, see problem2.py in same dir.
lista = ['']
for element in inlist:
    if (element == '\n'):
        lista.append('')
        continue
    lista[-1]=lista[-1]+element[:-1]+' '

risultato=0
for element in lista:
    if (len(element.split(' '))==9 or (len(element.split(' '))==8 and not ('cid' in element))):
        risultato += 1
print (risultato)