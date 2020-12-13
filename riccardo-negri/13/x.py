#!/usr/bin/env python
# Day 13 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  259
# Second part answer: 210612924879242

with open('input.txt', 'r') as f:
	file = f.read().split()

nums = file[1].split(',')
t = int(file[0])
while True:
	for num in nums:
		if num != 'x':
			if t%int(num) == 0:
				print("First part answer: ", int(num)*(t-int(file[0])))
				print("Second part answer: 210612924879242 - Read x.md to find out how I calculate it")
				exit()
	t += 1
