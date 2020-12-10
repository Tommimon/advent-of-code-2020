#!/usr/bin/env python
# Day 8 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 2003
# Second part answer: 1984

instructions = []
with open('input.txt', 'r') as f:
	for line in f.readlines():
		instructions.append([line.split()[0], line.split()[1]])
instructions.append(["end", 0])

pc = 0
acc = 0
already_runned = []
while pc not in already_runned:
	already_runned.append(pc)
	if instructions[pc][0] == 'acc':
		acc += int(instructions[pc][1])
		pc += 1
	elif instructions[pc][0] == 'jmp':
		pc += int(instructions[pc][1])
	elif instructions[pc][0] == 'nop':
		pc += 1
	else:
		print('Something went wrong')

print("First part answer: ", acc)

# some healthy bruteforce
for index in range(len(instructions)-1, 0, -1):
	
	# change single instruction
	if instructions[index][0] == 'nop':
		instructions[index][0] = 'jmp'
	elif instructions[index][0] == 'jmp':
		instructions[index][0] = 'nop'

	# print(index, " --> ", instructions[index])

	pc = 0
	acc = 0
	time = 0
	while time < 10000:			# 10000 should be big enough, if no solution is found try to increase it
		if instructions[pc][0] == 'acc':
			acc += int(instructions[pc][1])
			pc += 1
		elif instructions[pc][0] == 'jmp':
			pc += int(instructions[pc][1])
		elif instructions[pc][0] == 'nop':
			pc += 1
		elif instructions[pc][0] == 'end':
			print("Second part answer: ", acc)
			exit()
		else:
			print('Something went wrong')
		time += 1

	# undo changes
	if instructions[index][0] == 'nop':
		instructions[index][0] = 'jmp'
	elif instructions[index][0] == 'jmp':
		instructions[index][0] = 'nop'