# MIPS 32bit Program for Day 1 of Advent Of Code 2020 by Riccardo Negri
# Challenge: https://adventofcode.com/2020/day/1
# Developed using MARS: https://courses.missouristate.edu/KenVollmar/MARS/
# SYSCALL functions available in MARS: https://courses.missouristate.edu/KenVollmar/mars/Help/SyscallHelp.html
# Part one: find two numbers that add up to 2020 and then multiply them together
# My answer for part one: 988771 (833*1187)
# Part two: find three numbers that add up to 2020 and then multiply them together
# My answer for part two: 171933104 (1237*511*272)

.data

.eqv FILE_MAX_SIZE 1000		# used to set buffer size for reading	
.eqv NUMBERS_AMOUNT 200
.eqv NUMBERS_AMOUNT_BYTE 800	# 200 * 4 bytes
.eqv BACKSLASH_N 10

NUM_ARRAY: .space NUMBERS_AMOUNT_BYTE 			
BUFFER: .space FILE_MAX_SIZE
FILE_NAME: .asciiz "input"
WELCOME_STRING: .asciiz "Welcome to my first MIPS program ever attempting to solve day 1 of Advent Of Code 2020!\n"
PARSED_CORRECTLY: .asciiz "Parsed numbers hopefully correctly (I don't check if the file it's opened correctly or if it's not empty).\n"
LOOP_FAIL: .asciiz "My dear friend, I'm sorry to inform you that either you gave me an impossible list of integers or you are not a good programmer!\n"
PART1_LOOP_SUCCESS: .asciiz "My dear friend, you're the best!\n"
PART1_SUCCESS: .asciiz "Here's your result for the first part:\n"
PART2_LOOP_SUCCESS: .asciiz "\nMy dear friend, you're the best! Again ;)\n"
PART2_SUCCESS: .asciiz "Here's your result for the second part:\n"

.text
WELCOME:
	li $v0, 4			# 4 --> print_string
	la $a0, WELCOME_STRING		# $a0 = address of null-terminated string to print    
	syscall

##### READ FILE TO BUFFER #####
OPEN_FILE:
	li $v0, 13			# 13 --> open_file
	la $a0, FILE_NAME		# $a0 = address of null-terminated string containing filename
	li $a1, 0 			# $a1 = flags, 0 for read-only
	li $a2, 0		        # $a2 = mode, mode is ignored
	syscall				# file descriptor returned in $v0
	move $s7, $v0      		# save the file descriptor in $s7

READ_FILE:
	li $v0, 14			# 14 --> read_file
	move $a0, $s7			# $a0 = file descriptor
	la $a1, BUFFER 			# $a1 = address of input buffer
	li $a2, FILE_MAX_SIZE		# $a2 = maximum number of characters to read
	syscall				# $v0 contains number of characters read (0 if end-of-file, negative if error).

#PRINT_FOR_DEBUG:
#	li $v0, 4			# 4 --> print_string
#	la $a0, BUFFER			# $a0 = address of null-terminated string to print    
#	syscall

########## PARSE INPUT ##########
# $t0 the ADDRESS of BUFF
# $t1 the ADDRESS of VECTOR
# $t5 is the '\n' == 10
# $t6 is the multiplier
# $t7 is the thing read and manipulated
# $s1 is the current integer
PARSE_START: 
	la $t0, BUFFER
	la $t1, NUM_ARRAY
	li $t5, BACKSLASH_N
	li $t6, 1
	move $s1, $zero

PARSE_CICLE:
	lb $t7, ($t0)
	beq $t5, $t7, FOUND_BACKSLASH_N	# every number, except the last one, is followed by a '\n'
	beq $zero, $t7, END_PARSE_CICLE	# '\x00' ends the string to parse
	subi $t7, $t7, 48		# value of '0' in ASCII
	mult $s1, $t5			# multiply by 10 the prev partial number
	mflo $s1
	add $s1, $s1, $t7		# add together the partial number and the digit we just got	
	addi $t0, $t0, 1		# switch to next char
	j PARSE_CICLE

FOUND_BACKSLASH_N:			# finally it's time to save the full number in the array
	sw $s1, ($t1)			# save the full integer
#	li $v0, 1			# 1 --> print_int
#	move $a0, $s1
#	syscall				# print the item just added
	li $t6, 1			# reset to 1 the multiplier
	addiu $t0, $t0, 1 		# switch to next char
	addiu $t1, $t1, 4		# switch to next integer in the array
	move $s1, $zero 		# reset the value in $s1 so it can read a new number
	j PARSE_CICLE	

END_PARSE_CICLE:
	sw $s1, ($t1)			# save the LAST INTEGER integer (the last one doen't have a '\n' at the end)
#	li $v0, 1			# 1 --> print_int
#	move $a0, $s1
#	syscall				# print the item just added
	li $v0, 4			# 4 --> print_string
	la $a0, PARSED_CORRECTLY	# $a0 = address of null-terminated string to print    
	syscall

###### FIRST PART ######
# $s0 is the address used in the first iteration
# $s1 is the address used in the second iteration
# $s2 is the address of first element after the array (the condition used in the loop)
# $s3 it actual value to match --> 2020
PART1_INITIALIZE_LOOP:
	la $s0, NUM_ARRAY		# starting address of the array
	addiu $s2, $s0, NUMBERS_AMOUNT_BYTE
	li $s3, 2020
PART1_LOOP:
	move $s1, $s0			# this way we keep checking only numbers that are after
	jal PART1_INNER_LOOP			
	addiu $s0, $s0, 4		# iterate to next int
	beq $s0, $s2, PART1_END_LOOP_FAIL
	j PART1_LOOP
	
PART1_INNER_LOOP:
	addiu $s1, $s1, 4		# iterate to next int
	lw $t0, ($s0)			# load values
	lw $t1, ($s1)			
	add $t2, $t0, $t1		
	beq $s3, $t2, PART1_END_LOOP_SUCCESS	# check if we found the pair we're looking for
	bne $s1, $s2, PART1_INNER_LOOP
	jr $ra

PART1_END_LOOP_FAIL:
	li $v0, 4			# 4 --> print_string
	la $a0, LOOP_FAIL		# $a0 = address of null-terminated string to print    
	syscall
	li $v0, 10      		# End program
	syscall
	
PART1_END_LOOP_SUCCESS:
	li $v0, 4			# 4 --> print_string
	la $a0, PART1_LOOP_SUCCESS	# $a0 = address of null-terminated string to print    
	syscall
	mult $t0, $t1			# multiply the two numbers that sum up to 2020
	mflo $t2
	li $v0, 4			# 4 --> print_string
	la $a0, PART1_SUCCESS		# $a0 = address of null-terminated string to print    
	syscall
	li $v0, 1			# 1 --> print_int 
	move $a0, $t2
	syscall				# print the answer

###### SECOND PART ######
# $s0 is the address used in the first iteration
# $s1 is the address used in the second iteration
# $s2 is the address used in the third iteration
# $s3 is the address of first element after the array, the condition in the loop
# $s4 it actual value to match --> 2020
PART2_INITIALIZE_LOOP:
	la $s0, NUM_ARRAY		# starting address of the array
	addiu $s3, $s0, NUMBERS_AMOUNT_BYTE
	li $s4, 2020
	
PART2_LOOP:
	move $s1, $s0			# this way we keep checking only numbers that are after this
	beq $s0, $s3, PART2_END_LOOP_FAIL
	j PART2_INNER_LOOP			
LAZY: 	addiu $s0, $s0, 4		# iterate to next int
	j PART2_LOOP
	
PART2_INNER_LOOP:
	addiu $s1, $s1, 4		# iterate to next int
	beq $s1, $s3, LAZY		# I could use jal and jr, but it takes time 
	move $s2, $s1
	j PART2_INNER_INNER_LOOP	# this way we keep checking only numbers that are after this
	
PART2_INNER_INNER_LOOP:
	addiu $s2, $s2, 4		# iterate to next int
	beq $s2, $s3, PART2_INNER_LOOP
	lw $t0, ($s0)			# load values
	lw $t1, ($s1)
	lw $t2, ($s2)			
	add $t3, $t0, $t1
	add $t4, $t3, $t2		
	beq $s4, $t4, PART2_END_LOOP_SUCCESS	# check if we found the pair we're looking for	
	j PART2_INNER_INNER_LOOP
	
PART2_END_LOOP_FAIL:
	li $v0, 4			# 4 --> print_string
	la $a0, LOOP_FAIL		# $a0 = address of null-terminated string to print    
	syscall
	li $v0, 10      		# End program
	syscall
	
PART2_END_LOOP_SUCCESS:
	li $v0, 4			# 4 --> print_string
	la $a0, PART2_LOOP_SUCCESS	# $a0 = address of null-terminated string to print    
	syscall
	mult $t0, $t1			# multiply the two numbers that sum up to 2020
	mflo $t3
	mult $t2, $t3			
	mflo $t4
	li $v0, 4			# 4 --> print_string
	la $a0, PART2_SUCCESS		# $a0 = address of null-terminated string to print    
	syscall
	li $v0, 1			# 1 --> print_int 
	move $a0, $t4
	syscall				# print the answer
	li $v0, 10      		# End program
	syscall
