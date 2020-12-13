def lcm(array):
    ans = 1
    for el in array: ans *=el
    return ans

from math import ceil
from functools import reduce
with open('marcomole00/13/input.txt') as file:
    myTime, bus  = file.read().split('\n')
bus = bus.split(',')
myTime = int(myTime)
book = {}
clock = []
for id in bus:
   if id == 'x': continue
   else: id = int(id)
   minuti = ceil(myTime/id)*id - myTime
   clock.append(minuti)
   book[minuti] = id

print(book[min(clock)]*min(clock))

counter = 0
k = 0 
ids = [int(bus[0])]
for k in range(1, len(bus)):
    #print(k)
    if bus[k] == 'x': continue 
    while((counter+k) % int(bus[k]) != 0 or counter == 0):
        counter += lcm(ids)
        #print(counter)
    ids.append(int(bus[k]))

print(counter)