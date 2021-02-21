#how not to solve a problem under 11-12 hours
input = 389125467
max_l = 1000000
cups = list(map(lambda el: int(el), str(input))) #showoff
curr = cups[0]
cups.extend(list(range(10, 1000001)))
for i in range (10000000):
    ind = cups.index(curr)
    letters = []
    for y in range(3):
        letters.append(cups[ind-(max_l-y) +1])
        del cups[ind -(max_l-y) +1]
    dest = curr -1
    while(dest in letters and dest>0):
        dest -= 1
    if dest == 0:
        dest = max_l
        while dest in letters:
            dest -= 1
    ind_dest = cups.index(dest)
    cups = cups[:ind_dest+1] + letters + cups[ind_dest +1:]
    curr = cups[cups.index(curr)-max_l+1]
    
print(cups[cups.index(1) -max_l +1] * cups[cups.index(1) -max_l +2])