#Thanks Tommy for being able to use a debugger.
#Just so you don't do what I did, line 21 used to be:
#
# bags = otherBags.replace(" bag", "").replace("s","").replace(".\n","").split(", ")
#
#Pros: it does remove "s" of "bags" left from the previous replace of "bag".
#Cons: it also removes every other s.

import re
allowedBags = ["shiny gold"]
temp = ["shiny gold"]
gCounter = 0

with open("mynam3isg00d/7/input.txt") as file:
    rules = file.readlines()
    while True:
        allowedBags = temp.copy()
        for rule in rules:
            (mainBag, otherBags) = rule.split(" bags contain ")
            for color in allowedBags:
                if (color in mainBag) and ("no other" not in otherBags):
                    temp.remove(color)
                    bags = otherBags.replace(" bags", " bag").replace(" bag","").replace(".\n","").split(", ")
                    for bag in bags:
                        num = re.search(r'\d+', bag).group()
                        for x in range(int(num)):
                            gCounter += 1
                            temp.append(bag[2:])
        if allowedBags == temp:
            break
print(gCounter)