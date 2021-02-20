input = 215694783
cups = list(map(lambda el: int(el), str(input))) #showoff
curr = cups[0]
for i in range (100):
    # three consecutive elements from curr
    a, b, c = cups[cups.index(curr)-8], cups[cups.index(curr)-7], cups[cups.index(curr)-6]
    cups.remove(a)
    cups.remove(b)
    cups.remove(c)
    dest = curr -1
    while(dest not in cups and dest>0):
        dest -= 1
    if dest not in cups:
        dest = max(cups)
    cups = cups[:cups.index(dest)+1] + [a,b,c] + cups[cups.index(dest)+1:]
    curr = cups[cups.index(curr)-8]
    
print(str(cups[cups.index(1)+1:]+cups[:cups.index(1)])[1:-1].replace(', ',''))