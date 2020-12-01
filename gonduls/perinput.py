import os
i=0
inputf = open('input.txt', 'r')
inlist = inputf.readlines()
for element in inlist:
    inlist[i]=int(element[:-1])
    i+=1
print(inlist)