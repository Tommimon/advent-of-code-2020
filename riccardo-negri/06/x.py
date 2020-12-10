#!/usr/bin/env python
# Day 6 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 6457
# Second part answer: 3260

import string

count = 0
total_1 = 0
total_2 = 0
prev_letters = []
group = []
with open('input.txt', 'r') as f:
	for line in f.readlines():
		if line == '\n':
			for letter in string.ascii_letters:
				condition = True
				for line in group:
					if letter not in line:
						condition = False
				if condition:
					total_2 += 1
			total_1 += count
			count = 0
			prev_letters = []
			group = []
		else:
			for letter in string.ascii_letters:
				if (letter in line) and (letter not in prev_letters):
					count += 1
					prev_letters += letter
			group.append(line)

print("First part answer: ", total_1)
print("Second part answer: ", total_2)