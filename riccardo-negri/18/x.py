#!/usr/bin/env python
# Day 18 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  11297104473091
# Second part answer: 185348874183674

def get_endindex(expression):
	count = 0
	for index, char in enumerate(expression):
		if char == '(':
			count += 1
		elif char == ')':
			count -= 1
		if count == 0:
			return index 

def eval(expression, case = False):		# True for first part 
	while len(expression) != 1:
		if '(' in expression:
			substart = expression.index('(')
			subend = substart + get_endindex(expression[substart:])
			temp = eval(expression[substart+1:subend], case)
			expression = expression[:substart] + [temp] + expression[subend+1:]	
		else:
			if case:
				ind_plus, ind_times = -1, -1
				if '+' in expression:
					ind_plus = expression.index('+')
				if '*' in expression:
					ind_times = expression.index('*')
				if 0 < ind_plus < ind_times or ind_times == -1:	
					index = expression.index('+')
					temp = int(expression[index-1]) + int(expression[index+1])
				else:
					index = expression.index('*')
					temp = int(expression[index-1]) * int(expression[index+1])
				expression = expression[:index-1] + [temp] + expression[index+2:]		
			else:
				if '+' in expression:
					index = expression.index('+')
					temp = int(expression[index-1]) + int(expression[index+1])
					expression = expression[:index-1] + [temp] + expression[index+2:]
				else:
					index = expression.index('*')
					temp = int(expression[index-1]) * int(expression[index+1])
					expression = expression[:index-1] + [temp] + expression[index+2:]		
	return int(expression[0])

first, second = 0, 0
with open('input.txt', 'r') as f:
	for expression in f.readlines():
		expression = expression.strip().replace('(', '( ').replace(')', ' )').split(' ')
		first += eval(expression, True)
		second += eval(expression)
print("First part answer:  ", first)
print("Second part answer: ", second)