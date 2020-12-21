#!/usr/bin/env python
# Day 21 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  2072
# Second part answer: fdsfpg,jmvxx,lkv,cbzcgvc,kfgln,pqqks,pqrvc,lclnj

def get_input():
	with open('input.txt', 'r') as f:
		foods = []
		for line in f.readlines():
			ingredients, allergens = [], []
			line = line.strip().replace(')', '').replace(',', '').replace('contains', '').split('(')
			for ingredient in line[0].strip().split(' '):
				ingredients.append(ingredient)
			for allergen in line[1].strip().split(' '):
				allergens.append(allergen)	
			foods.append((ingredients, allergens))
		return foods

# The basic idea is that if a food contains an allergen and another food contains the same allergen,
# the possible ingredients that might cointain that allergen are the intersection between the ingredients of the two foods
foods = get_input()
used_allergens = set()
allergens_ingredients = dict()
for food in foods:
	for allergen in food[1]:
		if allergen not in used_allergens:
			allergens_ingredients[allergen] = set()
			for ingredient in food[0]:
				allergens_ingredients[allergen].add(ingredient)
			for other_food in foods:
				if allergen in other_food[1] and other_food != food:
					temp_set = set()
					for ingredient in allergens_ingredients[allergen]:
						if ingredient in other_food[0]:
							temp_set.add(ingredient)
					allergens_ingredients[allergen] = temp_set
			used_allergens.add(allergen)

dangerous_ingredients = set()
for key in allergens_ingredients:
	for ingredient in allergens_ingredients[key]:
		dangerous_ingredients.add(ingredient)

count = 0
for food in foods:
	for ingredient in food[0]:
		if ingredient not in dangerous_ingredients:
			count += 1
print("First part answer:  ", count)

already_found = set()
still_going = True
while still_going:
	still_going = False
	for allergen in allergens_ingredients:
		if len(allergens_ingredients[allergen]) == 1:
			already_found.add(next(iter(allergens_ingredients[allergen])))
		else:
			temp = set()
			for ingredient in allergens_ingredients[allergen]:
				if ingredient not in already_found:
					still_going = True
					temp.add(ingredient)
			allergens_ingredients[allergen] = temp

string = ""
for key in sorted(allergens_ingredients):
	string += next(iter(allergens_ingredients[key])) + ','
print("Second part answer: ", string[:-1])