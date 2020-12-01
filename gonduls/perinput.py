import os
inputf = open('input.txt', 'r')
inlist = inputf.readlines()
for element in inlist:
    inlist[inlist.index(element)]=int(element[:-1])
print(inlist)