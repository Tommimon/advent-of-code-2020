with open('marcomole00/9/input.txt')as file:
    lines = file.read().split('\n')
    lines = list(map(int,lines))
    for i in range(len(lines)-25):
        check = False
        k = i+25
        for j in range(25):
            #print(lines[k-j-1])
            for l in range(25):
                if (k == l): break
                if lines[k] == lines[k-j-1] +lines[k-l-1]:check = True
                #print(lines[k-j-1] +lines[k-l-1])
        if check == False:
            print('ijjjj', lines[k])
            endpoint = lines[k]
            linesBefore = lines[:k+1]
            break
    print(linesBefore[0], ' ', linesBefore[-1] )
    arrayNumbers = []
    n = 0
    for number in linesBefore:
        del arrayNumbers[:]
        end = False
        i= 0
        for i in range(len(linesBefore) -n):
            #print(len(linesBefore) -n)
            arrayNumbers.append(linesBefore[i+n])
            if sum(arrayNumbers) == endpoint:
                print('helo')
                end = True
                break
            elif sum(arrayNumbers) > endpoint: 
                break
        if end == True: 
            print(min(arrayNumbers) + max(arrayNumbers))
            break
        n = n+1