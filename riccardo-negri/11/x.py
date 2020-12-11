#!/usr/bin/env python
# Day 11 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 2338
# Second part answer: 2134

def get_matrix():
	y = 0
	matrix = []
	with open('input.txt', 'r') as f:
		for line in f.readlines():
			matrix.append([])
			for char in line.strip():
				matrix[y].append(char)
			y += 1
	return matrix

# set option to True if you want to check only the near seats
def visible_occupied_seats(y_coord, x_coord, matrix, option = False):
    count = 0
    cases = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    for case in cases:
        x = x_coord
        y = y_coord
        while True:
            x += case[0]
            y += case[1]
            if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix):
                break
            if matrix[y][x] == 'L':
            	break
            if matrix[y][x] == '#':
                count += 1
                break
            if option:
            	break
    return count

results = []
options = [True, False]
for option in options:
	matrix = get_matrix()
	occupied_seats = 0
	while True:
		changes_list = []
		change_in_occupied_seats = 0
		for y in range(0, len(matrix)):
			for x in range (0, len(matrix[0])):
				if matrix[y][x] == '#':
					count = visible_occupied_seats(y, x, matrix, option)
					if option and count >= 4:
						changes_list.append([y, x, 'L'])
						change_in_occupied_seats -= 1
					elif count >= 5:
						changes_list.append([y, x, 'L'])
						change_in_occupied_seats -= 1
				if matrix[y][x] == 'L':
					count = visible_occupied_seats(y, x, matrix, option)
					if count == 0:
						changes_list.append([y, x, '#'])
						change_in_occupied_seats += 1
		occupied_seats += change_in_occupied_seats
		if change_in_occupied_seats == 0:
			break
		for i in range (0, len(changes_list)):
			matrix[changes_list[i][0]][changes_list[i][1]] = changes_list[i][2]
	results.append(occupied_seats)
print("First part answer:  ", results[0])
print("Second part answer: ", results[1])