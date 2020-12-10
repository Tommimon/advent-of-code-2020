#!/usr/bin/env python
# Day 10 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 2046
# Second part answer: 1157018619904 (2*7*4*4*2*4*7*7*4*7*4*7*7*7*7*7*7)

numbers = []
with open('input.txt', 'r') as f:
		for line in f.readlines():
			numbers.append(int(line))

numbers.append(0)
numbers.append(max(numbers)+3)
numbers = sorted(numbers)

one_jolt = 0
three_jolt = 0
for index, num in enumerate(numbers):
	if index+1 < len(numbers):
		if numbers[index+1]-num == 1:
			one_jolt += 1
		elif numbers[index+1]-num == 3:
			three_jolt += 1

print("First part answer:  ", (one_jolt)*(three_jolt))

def number_of_possible_adapters_to_connect(index):
	count = 0
	for i in range(1,4):
		try:
			if numbers[index+i]-numbers[index] <= 3:
				count += 1
		except IndexError:
			return count
	return count

dictionary = {}
for index, num in enumerate(numbers):
	dictionary[num] = number_of_possible_adapters_to_connect(index)

# The input file has some fixed patterns.
# So I found out by hand the values for the three different patterns possible.
# The patterns are 1 2 1, 1 3 2 1, 1 3 3 2 1. To visualize them use print(dictionary).
# I don't care about the 1 because it doesn't generate any fork.
forks = 1
for index,num in enumerate(numbers):
	if dictionary[num] == 2:
		if dictionary[numbers[index-1]] == 3:
			if dictionary[numbers[index-2]] == 3:
				forks *= 7
			else:
				forks *= 4
		else:
			forks *= 2
print("Second part answer: ", forks)