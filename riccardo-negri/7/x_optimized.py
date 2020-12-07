#!/usr/bin/env python
# Day 7 solution of Advent Of Code 2020 by Riccardo Negri and Tommimon
# First part answer: 131
# Second part answer: 11261

def contains(rules, found, color):
    for r in rules:
        for elem in r[1:]:
            if color in elem:
                found.add(r[0])
                contains(rules, found, r[0])

def how_many_bags_inside(bag):
	index = Bags.index(bag)
	if "otherbags" in Content[index]:
		return 0
	count = 0
	for keyBag in Content[index].keys():
		count += how_many_bags_inside(keyBag)*Content[index][keyBag] + Content[index][keyBag]
	return count

# Part one import by Tommimon
with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' bags contain ', '.').replace(', ', '.').split('.')[:-1]
containGold = set()
contains(lines, containGold, 'shiny gold')

# Part two import by Riccardo Negri
Bags = []
Content = []
with open('input.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace(',','').replace('.','').split()
		Bags.append(line[0]+line[1])
		CurrContent = {}
		try:
			for i in range(4, 1000, 4):		# from 4 to a number big enough to read the full string
				if line[i] == 'no':
					CurrContent[str(line[i+1]+line[i+2])] = 0
				else:
					CurrContent[str(line[i+1]+line[i+2])] = int(line[i])
		except IndexError:
			pass
		Content.append(CurrContent)

# Part one by Tommimon
print("First part answer:  ", len(containGold))	

# Part two by Riccardo Negri		
print("Second part answer: ", how_many_bags_inside("shinygold"))