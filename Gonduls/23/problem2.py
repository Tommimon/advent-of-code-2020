input = 389125467
cups = list(map(lambda el: int(el), str(input))) #showoff
curr = cups[0]
cups.extend(list(range(10, 1000001)))
for i in range (10000000):
    print(i)
    # three consecutive elements from curr
    a, b, c = cups[cups.index(curr)-1000000 +1], cups[cups.index(curr)-1000000 +2], cups[cups.index(curr)-1000000 +3]
    cups.remove(a)
    cups.remove(b)
    cups.remove(c)
    dest = curr -1
    while(dest not in cups and dest>0):
        dest -= 1
    if dest not in cups:
        dest = max(cups)
    cups = cups[:cups.index(dest)+1] + [a,b,c] + cups[cups.index(dest)+1:]
    curr = cups[cups.index(curr)-1000000+1]
    
print(cups[cups.index(1) -1000000 +1] * cups[cups.index(1) -1000000 +2])