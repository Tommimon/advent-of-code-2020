#!/usr/bin/env python
# Day 23 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  49725386
# Second part answer: 538935646702

# Thanks to Tommimon for advising me to use linked lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def play(buffer_in, moves):
	List = LinkedList()
	track_nodes = dict()

	List.head = Node(buffer_in[0])
	track_nodes[buffer_in[0]] = List.head

	temp = List.head
	for el in buffer_in[1:]:
		temp.next = Node(el)
		track_nodes[el] = temp.next
		temp = temp.next
	temp.next = List.head

	max1 = max(buffer_in)
	max2 = max1-1
	max3 = max1-2

	current_cup = List.head
	for step in range(0, moves):
		next_cup = current_cup.next
		next_3_values = [next_cup.value, next_cup.next.value, next_cup.next.next.value]

		curr_value = current_cup.value
		curr_value -= 1
		while curr_value != 0:
			if curr_value not in next_3_values:
				dest_addr = track_nodes[curr_value]
				break
			curr_value -= 1
		if curr_value == 0 and max1 not in next_3_values:
			dest_addr = track_nodes[max1]
		elif curr_value == 0 and max2 not in next_3_values:
			dest_addr = track_nodes[max2]
		elif curr_value == 0 and max3 not in next_3_values:
			dest_addr = track_nodes[max3]

		temp = dest_addr.next
		dest_addr.next = next_cup
		new_next_for_curr = next_cup.next.next.next
		next_cup.next.next.next = temp
		current_cup.next = new_next_for_curr 

		current_cup = current_cup.next

	values = []
	node = current_cup
	while True:
		if node.value == 1:
			for _ in range(0, 8):
				node = node.next
				values.append(node.value)
			return values
		node = node.next

buffer_in = [7, 1, 6, 8, 9, 2, 5, 4, 3]
answer = play(buffer_in, 100)
string = ""
for c in answer:
	string += str(c)
print("First part answer: ", string)

for n in range(10, 1000001):
	buffer_in.append(n)
following_one = play(buffer_in, 10000000)
print("Second part answer: ", following_one[0] * following_one[1])