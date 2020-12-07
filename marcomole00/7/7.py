
myBag = 'shiny gold '
bags = set()
bags.add(myBag)
bagsTemp = bags.union() #during the iteration you can't change 
with open('marcomole00/7/input.txt') as file:
    rules = file.read().split('\n')
    while True:
        check = False
        for bag in bags:
            for line in rules:
                outerBag, innerBags = line.split(' bags contain ')
                if bag in innerBags: 
                    bagsTemp.add(outerBag)
        if len(bags) == len(bagsTemp):break
        bags = bags.union(bagsTemp)
        
bags.remove(myBag)
print(len(bags))
        
        
        


