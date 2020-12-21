print((lambda n:(len(n)-((max(n)+3-len(n))//2))*((max(n)+3-len(n))//2))([0]+list(map(int,open("i","r").read().split('\n')))))
