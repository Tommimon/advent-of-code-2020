#!/usr/bin/env python
# Day 17 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  362
# Second part answer: 1980

def get_coords():
	coords = []
	z_coord = 0
	w_coord = 0
	with open('input.txt', 'r') as f:
		y_coord = 0
		for line in f.readlines():
			for x_coord, char in enumerate(line.strip()):
				if char == '#':
					coords.append([x_coord, y_coord, z_coord, w_coord])
			y_coord += 1
	return coords, x_coord, y_coord

def active_neighbors(x,y,z,w, active_coords):
	count = 0
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				for h in [-1, 0, 1]:
					if not(j == 0 and k == 0 and i == 0 and h==0):
						if [x+i, y+j, z+k, w+h] in active_coords:
							count += 1
							if count > 3:
								return count
	return count

# Probably not the most efficient way to do this, but it executes in a reasonable time (about 4 min)
# Because I wanted to solve both parts with the same code, part 1 takes a little longer than what is really needed
for part in [False, True]:		# part one and two
	active_coords, x_coord, y_coord = get_coords()
	x_range = [0, x_coord+1]
	y_range = [0, y_coord]
	z_range = [0, 1]
	w_range = [0, 1]		# part two
	if not part:		
		w_range = [1, 0]	# part one
	for cycle in range(0, 6):
		new_active_coords = []
		for x in range(x_range[0]-1, x_range[1]+1):
			for y in range(y_range[0]-1, y_range[1]+1):
				for z in range(z_range[0]-1, z_range[1]+1):
					for w in range(w_range[0]-1, w_range[1]+1):
						active = active_neighbors(x,y,z,w, active_coords)
						if active == 2 or active == 3:
							if [x, y, z, w] in active_coords:
								new_active_coords.append([x,y,z,w])
							elif active == 3:
								new_active_coords.append([x,y,z,w])
		active_coords = new_active_coords
		x_range[0] -= 1
		y_range[0] -= 1
		z_range[0] -= 1
		x_range[1] += 1
		y_range[1] += 1
		z_range[1] += 1
		if part:		# part two
			w_range[0] -= 1
			w_range[1] += 1
		else:			# part one
			part1_answer = len(active_coords)

print("First part answer:  ", part1_answer)
print("Second part answer: ", len(active_coords))