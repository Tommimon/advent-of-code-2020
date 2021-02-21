input = 215694783
cups = list(map(lambda el: int(el), str(input))) #showoff
curr = cups[0]
for i in range (100):
    # three consecutive elements from curr
    three = [cups[cups.index(curr)-8], cups[cups.index(curr)-7], cups[cups.index(curr)-6]]
    for el in three:
        cups.remove(el)
    dest = curr -1
    while(dest in three and dest>0):
        dest -= 1
    if dest == 0:
        dest = max(cups)
    cups = cups[:cups.index(dest)+1] + three + cups[cups.index(dest)+1:]
    curr = cups[cups.index(curr)-8]
    
print(str(cups[cups.index(1)+1:]+cups[:cups.index(1)])[1:-1].replace(', ',''))