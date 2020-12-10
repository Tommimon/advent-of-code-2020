#It genuily could work, I wouldn't be able to tell you, it didn't end
with open('input.txt', 'r') as inputf:
        lista= list(map(int, inputf.read().split('\n')))
lista.append(0)
lista=sorted(lista)

def conta(parlist, offset = 0):
        #print(parlist, offset)
        partial = 1
        for i in range(len(parlist[1+offset:-1])):
                if (parlist[offset+i+2]-parlist[i+offset]<=3):
                        partial += conta(parlist[:i+1+offset]+parlist[i+2+offset:], i+offset)
        return partial

print(conta(lista))