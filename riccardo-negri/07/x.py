#!/usr/bin/env python
# Day 7 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 131
# Second part answer: 11261

def check_if_contains_shiny_gold(bag):
	index = Bags.index(bag)
	if "shinygold" in Content[index]:
		return True
	elif "otherbags" in Content[index]:
		return False
	else:
		for keyBag in Content[index].keys():
			if check_if_contains_shiny_gold(keyBag):
				return 	True
	return False

def how_many_bags_inside(bag):
	index = Bags.index(bag)
	if "otherbags" in Content[index]:
		return 0
	count = 0
	for keyBag in Content[index].keys():
		count += how_many_bags_inside(keyBag)*Content[index][keyBag] + Content[index][keyBag]
	return count

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

count = 0
for bag in Bags:
	if check_if_contains_shiny_gold(bag):
		count += 1

print("First part answer:  ", count)
print("Second part answer: ", how_many_bags_inside("shinygold"))