#!/usr/bin/env python
# Day 20 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  11788777383197
# Second part answer: 2242

import copy 
import math

def get_input():
	tiles = dict()
	with open('input.txt', 'r') as f:
		for line in f.readlines():
			if 'Tile' in line:
				tile_number = int(line[5:9])
				tiles[tile_number] = [[]]
				y = 0
			elif len(line)> 2:
				tiles[tile_number][0].append(line.strip())
	return tiles

def print_tile(tile):
	for line in tile:
		print("\n", line)

def flip_horizontally(tile):
	temp = tile.copy()
	for i in range(0,len(tile),1):
		tile[i] = tile[i][::-1]
	return temp

def flip_vertically(tile):
	temp = tile.copy()
	temp.reverse()
	return temp

def rotate(tile): 
	return [''.join(list(i)[::-1]) for i in zip(*tile)]

def border_values(tile_arrangements):
	values = set()
	for tile in tile_arrangements:	# calculated all the tops and bottoms
		values.add(left_border_value(tile))
		values.add(right_border_value(tile))
		values.add(top_border_value(tile))
		values.add(bottom_border_value(tile))
	return values

def left_border_value(tile):
	temp_left = ''
	for line in tile:
		temp_left += line[0]
	return int(temp_left.replace('.', '0').replace('#', '1'), base=2)

def right_border_value(tile):
	temp_right = ''
	for line in tile:
		temp_right += line[-1]
	return int(temp_right.replace('.', '0').replace('#', '1'), base=2)

def top_border_value(tile):
	return int(tile[0].replace('.', '0').replace('#', '1'), base=2)

def bottom_border_value(tile):
	return int(tile[-1].replace('.', '0').replace('#', '1'), base=2)

def common_borders_values(number_tile1, number_tile2):	
	values1 = border_values(tiles[number_tile1])
	values2 = border_values(tiles[number_tile2])
	c_values = set()
	for i in values1:
		if i in values2:
			c_values.add(i)
	assert(len(c_values) == 2)
	return c_values

def create_arrangements(tile):
	arrangements = []
	arrangements.append(tile)
	arrangements.append(flip_vertically(tile))
	arrangements.append(flip_horizontally(tile))
	new_arrangement = tile
	for i in range(0, 1):	# try to switch to 3 if no solution is found for part 2
		new_arrangement = rotate(new_arrangement)
		arrangements.append(new_arrangement)
		arrangements.append(flip_vertically(new_arrangement))
		arrangements.append(flip_horizontally(new_arrangement))
	return arrangements

def get_subtile(tile):
	subtile = []
	for i in range(1, 9):
		subtile.append(tile[i][1:9])
	return subtile

def get_monsters(tile):	# remeber that tile is a list of strings
	assert(len(tile) == len(tile[0]))
	count = 0
	for y in range(1, len(tile)-1):
		for x in range(0, len(tile)-19):
			if tile[y][x] == '#' and tile[y+1][x+1] == '#' and tile[y+1][x+4] == '#' and tile[y][x+5] == '#' and tile[y][x+6] == '#' and tile[y+1][x+7] == '#' and tile[y+1][x+10] == '#' and tile[y][x+11] == '#' and tile[y][x+12] == '#' and tile[y+1][x+13] == '#' and tile[y+1][x+16] == '#' and tile[y][x+17] == '#' and tile[y-1][x+18] == '#' and tile[y][x+18] == '#' and tile[y][x+19] == '#':
				count += 1
	return count

def count_hash_inside(tile):
	count = 0
	for line in tile:
		for char in line:
			if char == '#':
				count += 1
	return count

tiles = get_input()

# Instead of comparing the borders as strings, I transform the string into values considering '#' as bit 1 and '.' as bit 0
# I need to consider the flipped tiles to get all possible border values (rotate doesn't change the actual value of the border)
for tileID in tiles:
	tiles[tileID].append(flip_horizontally(tiles[tileID][0]))
	tiles[tileID].append(flip_vertically(tiles[tileID][0]))

tile_border_values = dict()
for tileID in tiles:
	tile_border_values[tileID] = border_values(tiles[tileID])

# Tiles at the edge of the image also have a border, but the outermost edges won't line up with any other tiles
borders = set()
corners = set()
for tileID in tiles:
	check1 = False
	check2 = False
	for value in tile_border_values[tileID]:
		count = 0
		for other_tile in tiles:
			if value in tile_border_values[other_tile] and other_tile != tileID:
				count += 1
		if count == 0:
			if check1:
				borders.add(tileID)
				if check2:
					corners.add(tileID)
				check2 = True
			check1 = True

part1 = 1
for i in corners:
	part1 *= i
print("First part answer:  ", part1)

# At this point I know all the tileIDs that are on the border of the image
neighbors = {}
for tileID in tiles:	# Find all the neighbors of every tielID
	neighbors[tileID] = set()
	for value in tile_border_values[tileID]:
		count = 0
		for other_tile in tiles:
			if value in tile_border_values[other_tile] and other_tile != tileID:
				count += 1
				neighbors[tileID].add(other_tile)

# Fill the matrix with the tileIDs based on their neighbors and knowing which are on the corner and border
MatrixDimension = int(math.sqrt(len(tiles))) # 12 for input, 3 for example
matrix = []
for i in range(0, MatrixDimension):
	matrix.append([-1]*MatrixDimension)	# initialize all the values with -1

matrix[0][0] = next(iter(corners))
already_placed = {matrix[0][0]}	# it's a set

for i in range(1, MatrixDimension):	# Fill the upper and left side
	for border in borders:	# top
		if matrix[0][i-1] in neighbors[border] and border not in already_placed:
			matrix[0][i] = border
			already_placed.add(border)
			break
	for border in borders:	# left
		if matrix[i-1][0] in neighbors[border] and border not in already_placed:
			matrix[i][0] = border
			already_placed.add(border)
			break

last_elem_ind = MatrixDimension-1
for i in range(1, MatrixDimension): # let's do right side and lower side
	for border in borders:	# bottom
		if matrix[last_elem_ind][i-1] in neighbors[border] and border not in already_placed:
			matrix[last_elem_ind][i] = border
			already_placed.add(border)
			break
	for border in borders:	# right
		if matrix[i-1][last_elem_ind] in neighbors[border] and border not in already_placed:
			matrix[i][last_elem_ind] = border
			already_placed.add(border)
			break

assert(len(already_placed) == (MatrixDimension*4-4))	# Make sure I got all the borders right

for i in range(1, MatrixDimension-1):	# now let's fill the inside
	for j in range(1,  MatrixDimension-1):
		for tielID in tiles:
			if matrix[i][j-1] in neighbors[tielID] and matrix[i-1][j] in neighbors[tielID] and tielID not in already_placed:
				matrix[i][j] = tielID
				already_placed.add(tielID)
				break

# At this point I know exactly where are all the tielsID are on the image. I create all their possible arrangements 
tiles_arrangements = {}	
for tile_number in tiles:
	tiles_arrangements[tile_number] = []
	for arrangement in tiles[tile_number]:
		tiles_arrangements[tile_number] += create_arrangements(arrangement)

already_placed = set()
arranged_tiles = dict()
# Find which arrangements are the correct ones. Probably I can do a nicer and shorter versions, but I don't have the time
for i in range(0, MatrixDimension):
	for j in range(0, MatrixDimension):
		if i < MatrixDimension-1 and j < MatrixDimension-1:	
			right_side_values = common_borders_values(matrix[i][j], matrix[i][j+1])
			bottom_side_values = common_borders_values(matrix[i][j], matrix[i+1][j])
			for arrangement in tiles_arrangements[matrix[i][j]]:
				right = right_border_value(arrangement)
				bottom = bottom_border_value(arrangement)
				if right in right_side_values and bottom in bottom_side_values:
					already_placed.add(matrix[i][j])
					arranged_tiles[matrix[i][j]] = arrangement
					break
		elif j == MatrixDimension-1 and i < MatrixDimension-1:  # last column
			left_side_values = common_borders_values(matrix[i][j], matrix[i][j-1])
			bottom_side_values = common_borders_values(matrix[i][j], matrix[i+1][j])
			for arrangement in tiles_arrangements[matrix[i][j]]:
				left = left_border_value(arrangement)
				bottom = bottom_border_value(arrangement)
				if left in left_side_values and bottom in bottom_side_values:
					already_placed.add(matrix[i][j])
					arranged_tiles[matrix[i][j]] = arrangement
					break
		elif i == MatrixDimension-1 and j < MatrixDimension-1:  # last row
			right_side_values = common_borders_values(matrix[i][j], matrix[i][j+1])
			top_side_values = common_borders_values(matrix[i][j], matrix[i-1][j])
			for arrangement in tiles_arrangements[matrix[i][j]]:
				right = right_border_value(arrangement)
				top = top_border_value(arrangement)
				if right in right_side_values and top in top_side_values:
					already_placed.add(matrix[i][j])
					arranged_tiles[matrix[i][j]] = arrangement
					break
		elif i == MatrixDimension-1 and j == MatrixDimension-1:	# bottom-right corner
			left_side_values = common_borders_values(matrix[i][j], matrix[i][j-1])
			top_side_values = common_borders_values(matrix[i][j], matrix[i-1][j])
			for arrangement in tiles_arrangements[matrix[i][j]]:
				left = left_border_value(arrangement)
				top = top_border_value(arrangement)
				if left in left_side_values and top in top_side_values:
					already_placed.add(matrix[i][j])
					arranged_tiles[matrix[i][j]] = arrangement
					break
assert(len(already_placed) == MatrixDimension**2)

# Merge the arranged tiles in a final arrangement
arrangement = [ ]
for i in range(0, MatrixDimension):
	for z in range(0, 8):	# 8 is the subtile width
		arrangement.append([])
	for j in range(0, MatrixDimension):
		sub = get_subtile(arranged_tiles[matrix[i][j]])
		for w in range(0, 8):
			arrangement[w+i*8].append(sub[w])
temp_arrangement = []
for line in arrangement:
	temp_line = ''
	for sub in line:
		temp_line += sub
	temp_arrangement.append(temp_line)
arrangement = temp_arrangement
assert(len(arrangement) == len(arrangement[0]))

# Create some arrangements of the final image to find the one that contains the monster
arrangements = create_arrangements(arrangement)

# Now we want to find the monsters and then calculate how many '#' are not covered by the monster 
		                  # 
		#    ##    ##    ###
		 #  #  #  #  #  #   
for arrangement in arrangements:
	num_monsters = get_monsters(arrangement)
	if num_monsters > 0:
		#print(arrangement)
		count = count_hash_inside(arrangement)
		print("Second part answer: ", count-num_monsters*15)
		exit()