#this one works like a charm, it's basically the same as problem2 but done in a smart way.
with open('input.txt', 'r') as inputf:
        lista= list(map(int, inputf.read().split('\n')))
lista.append(0)
lista=sorted(lista)
lista.append(lista[-1]+3)

#counts all possible combos having a step of three or lower from point a to point b in a specific list
def conta(parlist, offset = 0):
        partial = 1
        for i in range(len(parlist[1+offset:-1])):
                if (parlist[offset+i+2]-parlist[i+offset]<=3):
                        partial += conta(parlist[:i+1+offset]+parlist[i+2+offset:], i+offset)
                    #I am sorry for this if condition, it works so I stopped questioning it. Recursive function. Offset needed as not to count previous cases.
        return partial

#checks points where passage is mandatory
breakpoints = [0]
for i in range(len(lista)-1):
    if(-lista[i]+lista[i+1]>2):
        breakpoints.append(i)

#calculates number of total possible combos by multiplying combos in areas between breakpoints (mandatory points)
ris = 1
for i in range(len(breakpoints)-1):
    ris *= conta(lista[breakpoints[i]+1:breakpoints[i+1]+1])
print(ris)