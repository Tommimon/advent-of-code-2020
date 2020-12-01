with open('marcoparadina/input_d1.1.txt', 'r') as f:
    arr=[]
    ans=0
    for line in f:
        arr.append(int(line))
    for i in arr:
        for j in arr:
            if (i+j)==2020:
                ans=i*j
        
print(ans)