#!/usr/bin/env python
# Day 4 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer: 213
# Second part answer: 147

counter_1 = 0
counter_2 = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']		# cid not required
list_of_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

with open('input.txt', 'r') as f:
	text = f.read()
	text = text.split('\n\n')
	for data_set in text:
		check = True
		data = dict(subset.split(':') for subset in data_set.replace('\n',' ').split(' '))
		
		for field in required_fields:	# part one
			if field not in data:
				check = False
		
		if check:						# part two, enter only if we have all required fields
			counter_1 += 1
			for field in required_fields:
				if field == 'byr':
					if int(data.get(field)) < 1920 or int(data.get(field)) > 2002:
						check = False
				elif field == 'iyr':
					if int(data.get(field)) < 2010 or int(data.get(field)) > 2020:
						check = False
				elif field == 'eyr':
					if int(data.get(field)) < 2020 or int(data.get(field)) > 2030:
						check = False
				elif field == 'hgt':
					if data.get(field)[-2:] == 'cm':
						if int(data.get(field)[:-2]) < 150 or int(data.get(field)[:-2]) > 193:
							check = False
					elif data.get(field)[-2:] == 'in':
						if int(data.get(field)[:-2]) < 59 or int(data.get(field)[:-2]) > 76:
							check = False
					else:
						check = False
				elif field == 'hcl':
					if data.get(field)[:1] == '#':
						if len(data.get(field)[1:]) == 6:
							if data.get(field)[1:].strip("abcdef0123456789") != '':
								check = False
						else:
							check = False
					else:
						check = False
				elif field == 'ecl':
					if data.get(field) not in list_of_eye_colors:
						check = False
				elif field == 'pid':
					if len(data.get(field)) != 9:
						check = False
			if check:
				counter_2 += 1

print("First part answer:  ", counter_1)
print("Second part answer: ",counter_2)