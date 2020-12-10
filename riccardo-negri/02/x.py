#!/usr/bin/env python
# Day 2 solution of Advent Of Code 2020 by Riccardo Negri
# Part one solution:638 
# Part two solution:699

count_1 = 0
count_2 = 0
with open('input.txt', 'r') as f:
	for line in f.readlines():
		line = line.replace('-', ' ' )
		line = line.split(' ')
		if line[3].count(line[2][0]) >= int(line[0]) and line[3].count(line[2][0]) <= int(line[1]):
			count_1 += 1	# part one
		if (line[3][int(line[0])-1] == line[2][0]) ^ (line[3][int(line[1])-1] == line[2][0]):
			count_2 += 1	# part two
print('Part one solution:' + str(count_1))
print('Part two solution:' + str(count_2))