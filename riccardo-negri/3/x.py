#!/usr/bin/env python
# Day 3 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 153
# Second part answer: 2421944712

offsets = [[1,1], [3,1], [5,1], [7,1], [1,2]]	# x and y
skip = False
answer = 1

with open('input.txt', 'r') as f:
	for case in range(len(offsets)):
		counter = 0
		x_coord = 0
		skip = False
		for line in f.readlines():
			if (not skip):		# I use skip in case I need to increase y coordinates by more than one unit
				if offsets[case][1] == 2:
					skip = True	
				x_coord = x_coord % (len(line) - 1)
				if line[x_coord] == '#':
					counter += 1
				x_coord += offsets[case][0]
			else:
				skip = False
		offsets[case].append(counter)
		f.seek(0)

for x in range(len(offsets)):
	if x == 1:				# slope for part 1
		print("First part answer: " + str(offsets[x][2]))
	answer *= offsets[x][2]
print("Second part answer: " + str(answer))
