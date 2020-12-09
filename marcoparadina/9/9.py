with open ('marcoparadina/9/input9.txt') as f:
    arr=list(map(int, f.read().split('\n')))    #this took some documentation to find out
    #print(arr)

for i, value in enumerate(arr[25:]):
    valid=False
    for j in arr[i:i+25]:
        for k in arr[i:i+25]:
            if k!=j:
                if value==j+k:
                    valid=True
    if valid==False:
        invalid=value
                
for i in range(0,(len(arr)+1)):
    got_it=False
    continuous_sum=0
    candidate=[]
    for j in arr[i:]:
            continuous_sum+=j
            candidate.append(j)
            if continuous_sum==invalid:
                answer=max(candidate)+min(candidate)
                got_it=True
    if got_it:
        break   
    #This break is here because if you let the loop continue after findig one solution it 
    #finds a second one and i couldn't check if it is correct.
print('Solution to part 1:', invalid)
print('Solution to part 2:', answer)