myBag = 'shiny gold'
rules = []
midBags = set()
midBags.add(myBag)
#i've the feeling that never attended an algo class is making this too much fucking difficult
#pradella i'm ready

def part2(string):
    numberTemp = 1
    if string == myBag: numberTemp = 0
    for line in rules:
        outerBag, innerBags = line.split(' bags contain ')
        innerBags = innerBags.replace(', ', '.').replace('bags', '').replace('bag', '').split('.')[:-1]
        if outerBag == string:
            for idk in innerBags:
                if idk != 'no other ':
                    #print(idk)
                    idk = idk[:-1]
                    print(idk)
                    numberTemp += int(idk[0])*int(part2(idk[2:]))
    return(numberTemp)
            

def part1(rules):
    bags = set()
    bags.add(myBag)
    bagsTemp = bags.union() #during the iteration you can't change 
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

with open('marcomole00/7/input.txt') as file:
    rules = file.read().split('\n')
    part1(rules)
    #print(midBags)
    print(part2(myBag))
        
        
        
        


