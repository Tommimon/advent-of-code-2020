#!/usr/bin/env python
# Day 19 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  178
# Second part answer: 346

def get_matches(number_of_rule):
	if number_of_rule in inner_options:
		return inner_options[number_of_rule]
	else:
		matches = []
		if rules[number_of_rule][0][0] == 'b' or rules[number_of_rule][0][0] == 'a':
			return rules[number_of_rule][0][0]
		else:
			for pipe in rules[number_of_rule]:
				temp = []
				if len(pipe) == 1:
					temp = get_matches(pipe[0])
				elif len(pipe) == 2:
					temp1 = get_matches(pipe[0])
					temp2 = get_matches(pipe[1])
					for str1 in temp1:
						for str2 in temp2:
							temp.append(str1+str2)
				elif len(pipe) == 3:
					temp1 = get_matches(pipe[0])
					temp2 = get_matches(pipe[1])
					temp3 = get_matches(pipe[3])
					for str1 in temp1:
						for str2 in temp2:
							for str3 in temp3:
								temp.append(str1+str2+str3)
				matches += temp
		inner_options[number_of_rule] = matches
		return matches

def get_input():
	with open('input.txt', 'r') as f:
		received_messages = []
		rules = {}
		more_rules = True
		for line in f.readlines():
			if line == '\n':
				more_rules = False
				continue
			if more_rules:
				line = line.strip().replace(':', '').replace('"', '').split(' ')
				if '|' in line:
					rules[line[0]] = [[], []]
					switch = True
					for i in range(1, len(line)):
						if line[i] == '|':
							switch = False
							continue
						if switch:
							rules[line[0]][0].append(line[i])
						else:
							rules[line[0]][1].append(line[i])
				else:
					rules[line[0]] = [[]]
					for i in range (1, len(line)):
						rules[line[0]][0].append(line[i])
			else:
				received_messages.append(line.strip())
		return rules, received_messages

rules, received_messages = get_input()

inner_options = {}	# used in get_matches()
matches_strings = set(get_matches('0'))

count1, count2 = 0, 0
SECTION_LENGTH = 8	# 5 for example, 8 for input.txt
for message in received_messages:
	if message in matches_strings:
		count1 += 1
		count2 += 1
	else:		
		# 	need to check first part with "rule 8" and second part with "rule 11"
		#	8: 42 | 42 8
		#	11: 42 31 | 42 11 31
		for sub in range(0, int(len(message)/SECTION_LENGTH)+3 ):
			sub8 = message[:SECTION_LENGTH*sub]
			sub11 = message[SECTION_LENGTH*sub:]
			check8 = False
			if len(sub8) != 0 and len(sub11) != 0:
				check8 = True
				for i in range(SECTION_LENGTH, len(sub8)+SECTION_LENGTH, SECTION_LENGTH):
					if sub8[i-SECTION_LENGTH: i] not in inner_options['42']:
						check8 = False
				check11 = False
				if int(len(sub11))%(SECTION_LENGTH*2) == 0:
					check11 = True
					for i in range(SECTION_LENGTH, int(len(sub11)/2)+SECTION_LENGTH, SECTION_LENGTH):
						if sub11[i-SECTION_LENGTH: i] not in inner_options['42']:
							check11 = False
					for i in range((int(len(sub11)/2))+SECTION_LENGTH, len(sub11)+SECTION_LENGTH, SECTION_LENGTH):
						if sub11[i-SECTION_LENGTH: i] not in inner_options['31']:
							check11 = False
			if check8 and check11:
				count2 += 1
				break
print("First part answer:  ", count1)
print("Second part answer: ", count2)