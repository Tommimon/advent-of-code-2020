#!/usr/bin/env python
# Day 15 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  662
# Second part answer: 37312

with open('input.txt', 'r') as f:
	spoken_nums = list(map(int, f.read().split(',')))

to_find = [2020, 30000000]
temp_last = spoken_nums[-1]
keep_track_dict = {}
for index, num in enumerate(spoken_nums):
	keep_track_dict[num] = [index, index]
for counter in range(len(spoken_nums), max(to_find)):
	new_num = keep_track_dict[temp_last][1] - keep_track_dict[temp_last][0]
	try:
		keep_track_dict[new_num][0] = keep_track_dict[new_num][1]
		keep_track_dict[new_num][1] = counter
	except KeyError:
		keep_track_dict[new_num] = [counter, counter]
	spoken_nums.append(new_num)
	temp_last = new_num

print("First part answer:  ", spoken_nums[to_find[0]-1])
print("Second part answer: ", spoken_nums[to_find[1]-1])