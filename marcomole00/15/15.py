numbers = {
    14 : [1],
    8  : [2],
    16 : [3],
    0 : [4],
    1 : [5],
    17 : [6]
}

lastSaid = 17

for i in range(7,30000001): # 2021 for part1
    if len(numbers[lastSaid]) == 1:
        lastSaid = 0
        if 0 not in numbers:
            numbers[0] = [i]
        else: numbers[0].append(i)
    else: 
        temp =  numbers[lastSaid][-1] - numbers[lastSaid][-2]
        lastSaid = temp
        if lastSaid not in numbers:
            numbers[lastSaid] = [i]
        else: numbers[lastSaid].append(i)

print(lastSaid)

    
    