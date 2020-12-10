with open ('marcomole00/10/input.txt') as file:
    lines = list(map(int,file.read().split('\n')))
    lines.append(0)
    lines.append(max(lines)+3)
    lines.sort()
difference1 = 0
difference3 = 0 # my
difference2 = 0
comb = 1
for i in range(len(lines)-1):
    if lines[i+1] - lines[i] == 1: difference1+=1
    elif lines[i+1] - lines[i] == 3: difference3 +=1

risultati = {}
#sooo today i've learned a lot, firstly i'm an ignorant slut
#second: you can use a dictionary to store value during a recursive call and reduce by 10000000x the computation time
def distanza(i):
    if i == len(lines)-1:
         return 1
    if i in risultati: 
        return  risultati[i]
    ans = 0
    for j in range(i+1,len(lines)):
        if lines[j]-lines[i] <= 3:
            ans += distanza(j)
    risultati[i] = ans
    return ans
print(distanza(0))
#print(rec(0))
print(difference1* difference3) 

