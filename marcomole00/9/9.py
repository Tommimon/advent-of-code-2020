with open('marcomole00/9/input.txt')as file:
    lines = list(map(int,file.read().split('\n')))
    for i in range(len(lines)-25):
        check = False
        k = i+25
        for j in range(25):
            for l in range(25):
                if (k == l): break
                if lines[k] == lines[k-j-1] +lines[k-l-1]:check = True
        if check == False:
            print('first:', lines[k])
            endpoint = lines[k]
            break
    n = 0
    for number in lines:
        arrayNumbers = []
        end = False
        i= 0
        for i in range(len(lines) -n):
            arrayNumbers.append(lines[i+n])
            if sum(arrayNumbers) == endpoint:
                end = True
                break
            elif sum(arrayNumbers) > endpoint: 
                break
        if end == True: 
            print(min(arrayNumbers) + max(arrayNumbers))
            break
        n = n+1