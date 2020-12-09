#Part 1, I'm done with funny and quirky comments
#spending 3 hours for a missing s is not fun
#also it's Python, what's there to explain

allowedBags = {"shiny gold"}
temp = {"shiny gold"}

with open("mynam3isg00d/7/input.txt") as file:
    rules = file.readlines()
    while True:
        allowedBags = allowedBags.union(temp)
        for rule in rules:
            (mainBag, otherBags) = rule.split("bags contain")
            for color in allowedBags:
                if color in otherBags:
                    temp.add(mainBag)
        if len(allowedBags) == len(temp):
            break
allowedBags.remove("shiny gold")
print(len(allowedBags))