with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()
    for element in inlist:
        inlist[inlist.index(element)]=int(element)

somma = 2020

for element in inlist:
    if ((somma - element) in inlist[inlist.index(element)+1:]):
        break
print('Element found: '+ str(element)+'\nEnd result: '+ str(element * (somma-element)))