#!/usr/bin/env python
# Day 24 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  485
# Second part answer: 3933

floor = set() #  floor has only the black tiles coords
with open('input.txt', 'r') as f:
	for line in f.readlines():
		line = line.strip()
		x, y, ind = 0, 0, 0
		char = line[ind]
		while ind < len(line):
			char = line[ind]
			if char == 'e': x += 2
			elif char == 'w': x -= 2
			elif char == 'n':
				y += 2
				ind += 1
				char = line[ind]
				if char == 'e': x += 1
				else:	x -= 1
			else:
				y -= 2
				ind += 1
				char = line[ind]
				if char == 'e': x += 1
				else:	x -= 1
			ind += 1
		if (x, y) in floor:
			floor.remove((x, y))
		else:
			floor.add((x, y))

print("First part answer:  ", len(floor))

DAYS = 100
for day in range(0, DAYS):
	new_floor = set()
	whites = dict()
	for coords in floor:
		near_blacks = 0
		for dx in [-2, 2]:
			if (coords[0]+dx, coords[1]) in floor:
				near_blacks += 1
			else:
				if (coords[0]+dx, coords[1]) in whites:
					whites[(coords[0]+dx, coords[1])] += 1
				else:
					whites[(coords[0]+dx, coords[1])] = 1
		for dx in [-1, 1]:
			for dy in [-2, 2]:
				if (coords[0]+dx, coords[1]+dy) in floor:
					near_blacks += 1
				else:
					if (coords[0]+dx, coords[1]+dy) in whites:
						whites[(coords[0]+dx, coords[1]+dy)] += 1
					else:
						whites[(coords[0]+dx, coords[1]+dy)] = 1
		if not(near_blacks == 0 or near_blacks > 2):
			new_floor.add(coords)
	for coords in whites:
		if whites[coords] == 2:
			new_floor.add(coords)
	floor = new_floor

print("Second part answer: ", len(floor))