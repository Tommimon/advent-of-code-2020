#!/usr/bin/env python
# Day 16 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  29878
# Second part answer: 855438643439

switch = False
constraints = []
tickets = []
with open('input.txt', 'r') as f:
	for line in f.readlines():
		if not switch:
			try:
				constraints.append(list(map(int, (line[line.index(':')+2:]).strip().replace("or", '-').split('-') )))
			except ValueError:
				switch = True
		if switch:
			if line != '\n' and line != "your ticket:\n" and line != "nearby tickets:\n":
				tickets.append(list(map(int, line.strip().split(',') )))

real_tickets = []
error_rate = 0
for ticket in tickets:
	overall_satis = True
	for value in ticket:
		satis = False
		for constraint in constraints:
			if constraint[0] <= value <= constraint[1] or constraint[2] <= value <= constraint[3]:
				satis = True
		if not satis:
			overall_satis = False
			error_rate += value
	if overall_satis:
		real_tickets.append(ticket)
print("First part answer:  ", error_rate)

constraints_found = []
already_used_field_ID = []
last_field_ID = {}
matches = {}
while len(constraints_found) != len(constraints):
	possible_matches = {}
	for ind, constraint in enumerate(constraints):
		if ind not in constraints_found:
			possible_matches[ind] = 0
			for field_ID in range(0, len(tickets[0])):
				if field_ID not in already_used_field_ID:
					satis = True
					for ticket in real_tickets:
						value = ticket[field_ID]
						if not (constraint[0] <= value <= constraint[1] or constraint[2] <= value <= constraint[3]):
							satis = False
							break
					if satis:
						possible_matches[ind] += 1
						last_field_ID[ind] = field_ID
	for ind in possible_matches:
		if possible_matches[ind] == 1:
			constraints_found.append(ind)
			already_used_field_ID.append(last_field_ID[ind])
			matches[ind] = last_field_ID[ind]	# ind is the number of the constraint
			break

answer = 1
for i in range(0, 6):							# the 'departure' fields are the first six
	answer *= tickets[0][matches[i]]
print("Second part answer: ", answer)