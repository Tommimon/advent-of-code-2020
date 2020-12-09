found = False
sol = 0
with open("mynam3isg00d/9/input.txt") as file:
    nums = file.read().split('\n')
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for i in range(25, len(nums)):
        found = False
        toCheck = nums[i-25:i]
        toFind = nums[i]
        for x in toCheck:
            for y in toCheck:
                summ = x+y
                if (x+y == toFind) and (x != y):
                    found = True
                    break
            if found:
                break
        if not found:
            sol = nums[i]
            break
    
    print("Part 1: " + str(sol))

    found2 = False
    for i in range(len(nums)):
        toCheck2 = []
        counter = 0
        while sum(toCheck2) < sol:
            toCheck2.append(nums[i+counter])
            counter += 1
            if sum(toCheck2) == sol:
                found2 = True
                break
        if found2:
            print("Part 2: " + str(min(toCheck2) + max(toCheck2)))
            break