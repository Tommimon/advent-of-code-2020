#!/usr/bin/env python
# Day 17 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  362
# Second part answer: 1980

def get_coords():
	coords = set()
	with open('input.txt', 'r') as f:
		y_coord = 0
		for line in f.readlines():
			for x_coord, char in enumerate(line.strip()):
				if char == '#':
					coords.add((x_coord, y_coord, 0, 0))
			y_coord += 1
	return coords, x_coord, y_coord

def active_neighbors(x,y,z,w, active_coords):
	count = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				for h in [-1, 0, 1]:
					if not(j == 0 and k == 0 and i == 0 and h==0):
						if (x+i, y+j, z+k, w+h) in active_coords:
							count += 1
	return count

# I learned that sets, for this type of applications, are way better than lists becuase they are implemented using hash tables
for part in [True, False]:		# part one and two
	active_coords, x_coord, y_coord = get_coords()
	x_range = [0, x_coord+1]
	y_range = [0, y_coord]
	w_range = [0, 1]
	if part:
		w_range = [1, 0]
	for cycle in range(1, 7):
		new_active_coords = set()
		for x in range(x_range[0]-cycle, x_range[1]+cycle):
			for y in range(y_range[0]-cycle, y_range[1]+cycle):
				for z in range(0-cycle, 1+cycle):
					for w in range(w_range[0]-cycle, w_range[1]+cycle):
						active = active_neighbors(x,y,z,w, active_coords)
						if active == 2 or active == 3:
							if (x, y, z, w) in active_coords:
								new_active_coords.add((x,y,z,w))
							elif active == 3:
								new_active_coords.add((x,y,z,w))
		active_coords = new_active_coords
		if part:
			part1_answer = len(active_coords)
			w_range[0] += 1
			w_range[1] -= 1

print("First part answer:  ", part1_answer)
print("Second part answer: ", len(active_coords))