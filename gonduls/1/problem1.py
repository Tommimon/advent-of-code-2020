import os
i=0
inputf = open('input.txt', 'r')
inlist = inputf.readlines()
for element in inlist:
    inlist[i]=int(element[:-1])
    i+=1

somma = 2020

for element in inlist:
    if ((somma - element) in inlist[inlist.index(element)+1:]):
        break
print('Element found: '+ str(element)+'\nEnd result: '+ str(element * (somma-element)))