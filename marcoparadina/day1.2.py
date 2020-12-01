with open('marcoparadina/input_d1.1.txt', 'r') as f:
    arr=[]
    ans=0
    for line in f:
        arr.append(int(line))
    for i in arr:
        for j in arr:
            for k in arr:
                if (i+j+k)==2020:
                    ans=i*j*k
        
print(ans)