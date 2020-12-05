.data

.eqv FILE_MAX_SIZE 9382		# used to set buffer size for reading	
.eqv LETTERS_AMOUNT 10
.eqv LETTERS_AMOUNT_BYTE 12	# add 2: "\n" and misterious char
.eqv LINES 782
.eqv BACKSLASH_N 10
.eqv L_F 70
.eqv L_B 66
.eqv L_L 75
.eqv L_R 82

NUM_ARRAY: .space LETTERS_AMOUNT_BYTE
BUFFER: .space FILE_MAX_SIZE
BUFFER_LINE: .asciiz "0000000000\n"
FILE_NAME: .asciiz "input.txt"
WELCOME_STRING: .asciiz "Welcome to me copying riccardo from a different problem hoping to work things out!\n"
PARSED_CORRECTLY: .asciiz "Parsed \n"


.text
#WELCOME:
#	li $v0, 4			# 4 --> print_string
#	la $a0, WELCOME_STRING		# $a0 = address of null-terminated string to print    
#	syscall

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

# Close the file 
    li   $v0, 16       # system call for close file
    move $a0, $s7      # file descriptor to close
    syscall            # close file

#PRINT_FOR_DEBUG:
#	li $v0, 4			# 4 --> print_string
#	la $a0, BUFFER			# $a0 = address of null-terminated string to print    
#	syscall

#PRINT_ONLY_STRINGS:
    li $s1, LINES		#outside for, up to lines number
    move $t0, $zero     #outside for, t0 is index
START_PRINT:			#outside for
    bge $t0, $s1, ENDPRINT
	li $s2,	10#LETTERS_AMOUNT_BYTE #inside for, up to characters in line
	move $t1, $zero		#inside for, t1 is index
START_COPYING:			#inside for
	bge $t1, $s2, ENDCOPY
	la $t2, BUFFER_LINE #t2 = &buff line
	addu $t2, $t2, $t1  #t2 = &(buff line + t1)
	la $t3, BUFFER		#t3 = &buff
	addu $t3, $t3, $t1  #t3 = &(buff + t1)
	li $t4, LETTERS_AMOUNT_BYTE #t4 = 12
	mul $t4, $t4, $t0	#t4 = 12 * t0
	addu $t3, $t3, $t4	#t3 = &(buff + t1 + 12*t0)
	lb $t4, ($t3)		#loads byte from t3 
	sb $t4, ($t2)		#stores byte from from load
	addi $t1, $t1, 1	#t1 ++
	j START_COPYING
ENDCOPY:
#	la $t4, ENDING
#	lb $t4, 1($t2)
#	addiu $t4, $t4, 1
#	lb $t4, 2($t2)
	li $v0, 4
    la $a0, BUFFER_LINE
	syscall
	addi $t0, $t0, 1	#t0 ++

	j START_PRINT
ENDPRINT:


########## PARSE INPUT ##########
# $t0 the ADDRESS of BUFF
# $t1 the ADDRESS of VECTOR
# $t5 is the '\n' == 10
# $t6 is the multiplier
# $t7 is the thing read and manipulated
# $s1 is the current integer
#PARSE_START: 
#	la $t0, BUFFER
#	la $t1, NUM_ARRAY
#	li $t5, BACKSLASH_N
#	li $t6, 1
#	move $s1, $zero
#
#PARSE_CICLE:
#	lb $t7, ($t0)
#	beq $t5, $t7, FOUND_BACKSLASH_N	# every number, except the last one, is followed by a '\n'
#	beq $zero, $t7, END_PARSE_CICLE	# '\x00' ends the string to parse
##	subi $t7, $t7, 48		# value of '0' in ASCII
##	mult $s1, $t5			# multiply by 10 the prev partial number
#	mflo $s1
#	add $s1, $s1, $t7		# add together the partial number and the digit we just got	
#	addi $t0, $t0, 1		# switch to next char
#	j PARSE_CICLE
#
#FOUND_BACKSLASH_N:			# finally it's time to save the full number in the array
#	sw $s1, ($t1)			# save the full integer
##	li $v0, 1			# 1 --> print_int
##	move $a0, $s1
##	syscall				# print the item just added
#	li $t6, 1			# reset to 1 the multiplier
#	addiu $t0, $t0, 1 		# switch to next char
#	addiu $t1, $t1, 4		# switch to next integer in the array
#	move $s1, $zero 		# reset the value in $s1 so it can read a new number
#	j PARSE_CICLE	
#
#END_PARSE_CICLE:
#	sw $s1, ($t1)			# save the LAST INTEGER integer (the last one doen't have a '\n' at the end)
##	li $v0, 1			# 1 --> print_int
##	move $a0, $s1
##	syscall				# print the item just added
#	li $v0, 4			# 4 --> print_string
#	la $a0, PARSED_CORRECTLY	# $a0 = address of null-terminated string to print    
#	syscall

	li $v0, 10      		# End program
	syscall
