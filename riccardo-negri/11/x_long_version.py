#!/usr/bin/env python

# DON'T TAKE THIS CODE SERIOUSLY
# IT LOOKS REALLY BAD AND IT IS BAD, BUT IT WORKS

y = 0
matrix = []
with open('input.txt', 'r') as f:
	for line in f.readlines():
		matrix.append([])
		for char in line:
			if char != '\n':
				matrix[y].append(char)
		y += 1

prev_occupied_seats = None
while True:
	matrix_new = matrix
	occupied_seats = 0
	for y in range(0, len(matrix)):
		for x in range (0, len(matrix[0])):
			if matrix[y][x] == '#':
				occupied_seats += 1
	if prev_occupied_seats == occupied_seats:
		break
	prev_occupied_seats = occupied_seats

	mod_list = []
	mod_list.clear()
	for y in range(0, len(matrix)):
		for x in range (0, len(matrix[0])):
			if matrix[y][x] == '.':
				None 

			elif matrix[y][x] == 'L':
				count = 0
				if y-1 >= 0 and x-1 >= 0:
					if matrix[y-1][x-1] == '#':
						count += 1
				if y-1 >= 0:	
					if matrix[y-1][x] == '#':
						count += 1
				if y-1 >= 0 and x+1 < len(matrix[0]):	
					if matrix[y-1][x+1] == '#':
						count += 1
				if x-1 >= 0:	
					if matrix[y][x-1] == '#':
						count += 1
				if x+1 < len(matrix[0])	:
					if matrix[y][x+1] == '#':
						count += 1
				if y+1 < len(matrix) and x-1 >= 0:
					if matrix[y+1][x-1] == '#':
						count += 1
				if y+1 < len(matrix):	
					if matrix[y+1][x] == '#':
						count += 1
				if y+1 < len(matrix) and x+1 < len(matrix[0]):	
					if matrix[y+1][x+1] == '#':
						count += 1
				if count == 0:
					mod_list.append(x)
					mod_list.append(y)
					mod_list.append('#')		

			elif matrix[y][x] == '#':
				count = 0
				if y-1 >= 0 and x-1 >= 0:
					if matrix[y-1][x-1] == '#':
						count += 1
				if y-1 >= 0:	
					if matrix[y-1][x] == '#':
						count += 1
				if y-1 >= 0 and x+1 < len(matrix[0]):	
					if matrix[y-1][x+1] == '#':
						count += 1
				if x-1 >= 0:	
					if matrix[y][x-1] == '#':
						count += 1
				if x+1 < len(matrix[0])	:
					if matrix[y][x+1] == '#':
						count += 1
				if y+1 < len(matrix) and x-1 >= 0:
					if matrix[y+1][x-1] == '#':
						count += 1
				if y+1 < len(matrix):	
					if matrix[y+1][x] == '#':
						count += 1
				if y+1 < len(matrix) and x+1 < len(matrix[0]):	
					if matrix[y+1][x+1] == '#':
						count += 1
				if count >= 4:
					mod_list.append(x)
					mod_list.append(y)
					mod_list.append('L')

	for i in range (0, len(mod_list), 3):
		matrix[mod_list[i+1]][mod_list[i]] = mod_list[i+2]
print("First part answer:  ", occupied_seats)

y = 0
matrix = []
with open('input.txt', 'r') as f:
	for line in f.readlines():
		matrix.append([])
		for char in line:
			if char != '\n':
				matrix[y].append(char)
		y += 1

prev_occupied_seats = None
while True:
	matrix_new = matrix
	occupied_seats = 0
	for y in range(0, len(matrix)):
		for x in range (0, len(matrix[0])):
			if matrix[y][x] == '#':
				occupied_seats += 1
	if prev_occupied_seats == occupied_seats:
		break
	prev_occupied_seats = occupied_seats

	mod_list = []
	mod_list.clear()
	for y in range(0, len(matrix)):
		for x in range (0, len(matrix[0])):
			if matrix[y][x] == '.':
				None 

			elif matrix[y][x] == 'L':
				count = 0
				i = 1
				ycurr = y-i
				xcurr = x-i
				while y-i >= 0 and x-i >= 0 and matrix[y-i][x-i]=='.':
					i += 1
					ycurr = y-i
					xcurr = x-i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y-i
				xcurr = x
				while y-i >= 0 and matrix[y-i][x]=='.':
					i += 1
					ycurr = y-i
					xcurr = x
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y-i
				xcurr = x+i
				while y-i >= 0 and x+i < len(matrix[0]) and matrix[y-i][x+i]=='.':
					i += 1
					ycurr = y-i
					xcurr = x+i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y
				xcurr = x-i
				while x-i >= 0 and matrix[y][x-i]=='.':
					i += 1
					ycurr = y
					xcurr = x-i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y
				xcurr = x+i
				while x+i < len(matrix[0]) and matrix[y][x+i]=='.':
					i += 1
					ycurr = y
					xcurr = x+i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y+i
				xcurr = x-i
				while x-i >= 0 and y+i < len(matrix) and matrix[y+i][x-i]=='.':
					i += 1
					ycurr = y+i
					xcurr = x-i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y+i
				xcurr = x
				while y+i < len(matrix) and matrix[y+i][x]=='.':
					i += 1
					ycurr = y+i
					xcurr = x
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y+i
				xcurr = x+i
				while y+i < len(matrix) and x+i < len(matrix[0]) and matrix[y+i][x+i]=='.':
					i += 1
					ycurr = y+i
					xcurr = x+i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				if count == 0:
					mod_list.append(x)
					mod_list.append(y)
					mod_list.append('#')		

			elif matrix[y][x] == '#':
				count = 0
				i = 1
				ycurr = y-i
				xcurr = x-i
				while y-i >= 0 and x-i >= 0 and matrix[y-i][x-i]=='.':
					i += 1
					ycurr = y-i
					xcurr = x-i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y-i
				xcurr = x
				while y-i >= 0 and matrix[y-i][x]=='.':
					i += 1
					ycurr = y-i
					xcurr = x
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y-i
				xcurr = x+i
				while y-i >= 0 and x+i < len(matrix[0]) and matrix[y-i][x+i]=='.':
					i += 1
					ycurr = y-i
					xcurr = x+i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y
				xcurr = x-i
				while x-i >= 0 and matrix[y][x-i]=='.':
					i += 1
					ycurr = y
					xcurr = x-i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y
				xcurr = x+i
				while x+i < len(matrix[0]) and matrix[y][x+i]=='.':
					i += 1
					ycurr = y
					xcurr = x+i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y+i
				xcurr = x-i
				while x-i >= 0 and y+i < len(matrix) and matrix[y+i][x-i]=='.':
					i += 1
					ycurr = y+i
					xcurr = x-i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y+i
				xcurr = x
				while y+i < len(matrix) and matrix[y+i][x]=='.':
					i += 1
					ycurr = y+i
					xcurr = x
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				i = 1
				ycurr = y+i
				xcurr = x+i
				while y+i < len(matrix) and x+i < len(matrix[0]) and matrix[y+i][x+i]=='.':
					i += 1
					ycurr = y+i
					xcurr = x+i
				if ycurr >= 0 and xcurr >= 0 and ycurr < len(matrix) and xcurr < len(matrix[0]):
					if matrix[ycurr][xcurr] == '#':
						count += 1
				if count >= 5:
					mod_list.append(x)
					mod_list.append(y)
					mod_list.append('L')

	for i in range (0, len(mod_list), 3):
		matrix[mod_list[i+1]][mod_list[i]] = mod_list[i+2]
print("Second part answer: ", occupied_seats)