#!/usr/bin/env python
# Day 25 solution of Advent Of Code 2020 by Riccardo Negri
# Puzzle answer: 5414549

def get_loopsize(to_match, subj_num=7):
	value, loop_size = 1, 0
	while True:
		loop_size += 1
		value *= subj_num
		value %= 20201227
		if value == to_match:
			return loop_size

with open('input.txt', 'r') as f:
	pub_keys = list(map(int, f.read().split()))

value = 1
for _ in range(0, get_loopsize(pub_keys[0])):
	value *= pub_keys[1]
	value %= 20201227
print("Puzzle answer:", value)