#!/usr/bin/env python
# Day 22 solution of Advent Of Code 2020 by Riccardo Negri
# First part answer:  33010
# Second part answer: 32769

def get_input():
	with open('input.txt', 'r') as f:
		file = list(map(int, f.read().replace('Player 1:', '').replace('Player 2:', '').strip().split()))
		return file[:int(len(file)/2)], file[int(len(file)/2):]

def new_game(deck1, deck2, game=1):
	prev1 = set()
	prev2 = set()
	while len(deck1) != 0 and len(deck2) != 0:
		hash1, hash2 = hash(tuple(deck1)), hash(tuple(deck2))
		if hash1 in prev1 or hash2 in prev2:
			return 1	# winner is player 1
		prev1.add(hash1)
		prev2.add(hash2)
		play1, play2 = deck1[0], deck2[0]
		if len(deck1)-1 >= play1 and len(deck2)-1 >= play2:
			del deck1[0]
			del deck2[0]
			winner = new_game(deck1[:play1], deck2[:play2], game+1)
		else:
			winner = 2
			if play1 > play2:
				winner = 1
			del deck1[0]
			del deck2[0]
		if winner == 1:
			deck1.extend((play1, play2))
		else:
			deck2.extend((play2, play1))
	winner = 2
	if len(deck1) != 0:
		winner = 1
	if game == 1:
		return deck1, deck2
	return winner

def get_score(deck1, deck2):
	score = 0
	if len(deck1) != 0:
		for index, card in enumerate(deck1):
			score += card*(len(deck1)-index)
	else:
		for index, card in enumerate(deck2):
			score += card*(len(deck2)-index)
	return score

deck1, deck2 = get_input()
while len(deck1) != 0 and len(deck2) != 0:
	play1, play2 = deck1[0], deck2[0]
	del deck1[0]
	del deck2[0]
	if play1 > play2:
		deck1.extend((play1, play2))
	else:
		deck2.extend((play2, play1))
print("First part answer:  ", get_score(deck1, deck2))

deck1, deck2 = get_input()
deck1, deck2 = new_game(deck1, deck2)
print("Second part answer:  ", get_score(deck1, deck2))