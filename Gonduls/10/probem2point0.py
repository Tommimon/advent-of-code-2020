with open('input.txt', 'r') as inputf:
        lista= list(map(int, inputf.read().split('\n')))
lista.append(0)
lista=sorted(lista)

def conta(parlist, offset = 0):
        #print(parlist, offset)
        partial = 1
        for i in range(len(parlist[1+offset:-1])):
                
print(conta(lista))