#!/usr/bin/env python
# Day 14 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  14954914379452
# Second part answer: 3415488160714
  
def replace_bit(number, bit, position):
    mask = 1 << position 	# shift
    return (number & ~mask) | ((bit << position) & mask) 

def get_sum(dictionary):
	sum = 0
	for key in dictionary:
		sum += dictionary[key]
	return sum

with open('input.txt', 'r') as f:
	file = f.read().replace('=', '').replace('mem[', ' ').replace(']','').replace('mask', '-1').split()

dictionary = {}
for index, addr in enumerate(file):
	if index%2 == 0:
		addr = int(addr)
		if addr == -1:		#it's a mask
			curr_mask = file[index+1]
		else:
			value = int(file[index+1])
			for index2, char in enumerate(curr_mask):
				if char != 'X':
					value = replace_bit(value, int(char), 36-index2-1)
			dictionary[addr] = value

print("First part answer:  ", get_sum(dictionary))

dictionary = {}
for index, addr in enumerate(file):
	if index%2 == 0:
		addr = int(addr)
		if addr == -1:		#it's a mask
			curr_mask = file[index+1]
		else:
			addr_list=[]
			addr_list.append(addr)
			for index2, char in enumerate(curr_mask):
				addr_list_new = []
				if char == '1':
					for addr in addr_list:
						addr_list_new.append(replace_bit(addr, int(char), 36-index2-1))
					addr_list = addr_list_new
				elif char == 'X':
					for bit in [0,1]:
						for addr in addr_list:
							addr_list_new.append(replace_bit(addr, bit, 36-index2-1))
					addr_list = addr_list_new
			for addr in addr_list:
				dictionary[addr] = int(file[index+1])
				
print("Second part answer: ", get_sum(dictionary))
