import os
inputf = open('input.txt', 'r')
inlist = inputf.readlines()
for element in inlist:
    inlist[inlist.index(element)]=int(element[:-1])
    #print(element[:-1])

somma = 2020
exitv = 0

for element1 in inlist:
    for element2 in inlist[inlist.index(element1)+1:]:
        #print ('element1: ' + str(element1) + '\telement2: ' + str(element2))
        if ((somma - element1 - element2) in inlist[inlist.index(element2)+1:]):
            exitv = 1
            break
    if (exitv):
        break

print('Element1 found: '+ str(element1)+'\tIndex: '+ str(inlist.index(element1)))
print('Element2 found: '+ str(element2)+'\tIndex: '+ str(inlist.index(element2)))
print('Element3 found: '+ str(somma - element1 - element2)+'\tIndex: '+ str(inlist.index(somma - element1 - element2)))
print('End result: ' + str(element1 * element2 * (somma - element1 - element2)))
