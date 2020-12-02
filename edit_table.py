#!/usr/bin/env python
import re
import time 

username = None
day = None
solve = None
real_usernames = []

#def get_usernames():
#	global real_usernames
#
#	for line in lines:
#		if "Day |" in line:
#			usernames = re.search(r"\[.+]", line)
#			usernames = usernames.group()
#			usernames = usernames.replace('|', ' ')
#			usernames = usernames[1:].split('[')
#			for user in usernames:
#				if (usernames.index(user) % 2) == 0:
#					real_usernames.append(user[:-1])
#			break

def get_usernames():
	global real_usernames

	for line in lines:
		if "Day |" in line:
			usernames = line.replace("</sub></sup>", " <sup><sub>").split("<sup><sub>")
			for user in usernames:
				if (usernames.index(user) % 2) == 1:
					real_usernames.append(user)
			break



def get_data_from_user():
	global username
	global day
	global solve

	print("These are the users currently registered, if your username doesn't appear here contact the admin @Tommimon")
	for user in real_usernames:
		print("--> [" + str(real_usernames.index(user)) + "] " + user)

	while True:
		try:
			username = input("\nEnter your user ID or username: ")
			if (username in real_usernames) or (int(username) in range(0, len(real_usernames))):	
				if int(username) in range(0, len(real_usernames)):
					username = real_usernames[int(username)]
				break
			print("You must insert a correct user ID or username!")
		except ValueError:	
			print("You must insert a correct user ID or username!")
			continue

	while True:
		try:
			day = int(input("\nEnter the day you want to update: "))
			if day>=1 and day<=25:
				break
			print("You must insert a correct day!")
					
		except ValueError:
			print("It seems that you don't know what a number is")

	solve = input("""\nDid you solve the first part or both? (" " or "*" or "**"): """)
	while solve != "*" and solve != "**" and solve != " " and solve != "":
		print("You must insert a correct value!")
		solve = input("""\nDid you solve othe first part or both? (" " or "*" or "**"): """)
	if solve == '*':
		solve = '* '
	if solve == ' ':
		solve = '  '
	if solve == '':
		solve = '  '


def waiting_animation():
	animation = [
	"[                ]",
	"[>               ]",
	"[=>              ]",
	"[==>             ]",
	"[===>            ]",
	"[====>           ]",
	"[=====>          ]",
	"[======>         ]",
	"[=======>        ]",
	"[========>       ]",
	"[=========>      ]",
	"[==========>     ]",
	"[===========>    ]",
	"[============>   ]",
	"[=============>  ]",
	"[==============> ]",
	"[===============>]",
	"[================]",
	]
	notcomplete = True
	i = 0

	while notcomplete:
		print(animation[i % len(animation)], end='\r')
		time.sleep(.06)
		i += 1
		if i == 18:
			break

def is_this_the_line(line, day):
	try:
		if int(line[1:3]) == int(day):
			return True
	except ValueError:
		pass

def edit_line(line, userid, stars):
    search = '][u'
    if userid < 10:
        search += '0' + str(userid)
    else:
        search += str(userid)
    parts = line.split(search)
    parts[0] = parts[0][0:-2]  # remove stars or blank spaces
    line = parts[0] + stars + search + parts[1]
    return line

if __name__ == "__main__":    
	with open('README.md', 'r+') as f:
		# read file
		lines = f.read().splitlines()
		
		# manipulate lines with changes
		get_usernames()
		get_data_from_user()

		solve_text = solve
		if solve == '  ' or solve == ' ' or solve == '':
			solve_text = 'None'

		print("\nUpdating these info to the table at the speed of light (or almost)\n-->\tUser:\t" + str(username) + "\n-->\tDay:\t" + str(day) + "\n-->\tStars:\t" + str(solve_text) )
		
		# write back
		f.seek(0)
		for line in lines:
			condition = is_this_the_line(line, day)
			if condition:
				line = edit_line(line, real_usernames.index(username)+1, solve)
				print(line, file=f)
			else:
				print(line, file=f)
		
		waiting_animation()		# just because it's cool

		print("\nUpdated successfully, now you can push the file.\nSee you next time! ;)")