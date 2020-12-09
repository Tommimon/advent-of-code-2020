#!/usr/bin/env python
# Day 9 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 1492208709
# Second part answer: 238243506

def get_input(numbers):
	with open('input.txt', 'r') as f:
		for line in f.readlines():
			numbers.append(int(line))

def get_combinations(preamble, combinations):
	for x in preamble:
		for y in preamble:
			if x != y:
				combinations.append(x+y)

preamble_size = 25
numbers = []
get_input(numbers)

index = preamble_size
while True:
	combinations = []
	get_combinations(numbers[index-preamble_size:index], combinations)
	if numbers[index] not in combinations:
		first_part = numbers[index]
		print("First part answer: ", first_part)		
		break
	index += 1

index = 0
while True:
	inner_index = index
	add = 0
	while add < first_part:
		add += numbers[inner_index]
		inner_index += 1
	if add == first_part:
		numbers_sorted = sorted(numbers[index:inner_index])
		print("Second part answer: ", numbers_sorted[0]+numbers_sorted[-1])
		break
	index += 1