.data

.eqv FILE_MAX_SIZE 9382		# used to set buffer size for reading	
.eqv LETTERS_AMOUNT 10
.eqv LETTERS_AMOUNT_BYTE 12	# add 2: "\n" and misterious char
.eqv LINES 782
.eqv L_F 70
.eqv L_B 66
.eqv L_L 75
.eqv L_R 82

NUM_ARRAY: .space LETTERS_AMOUNT_BYTE
BUFFER: .space FILE_MAX_SIZE
BUFFER_LINE: .asciiz "0000000000\n"
FILE_NAME: .asciiz "input.txt"
END: .asciiz "\n"
PARSED_CORRECTLY: .asciiz "Parsed \n"
TEMPORARY: .space 4
RESULT: .space 4

.text

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

#Actual program
	la $s0, BUFFER_LINE
	la $s1, TEMPORARY
	la $s2, RESULT
    li $t7, LINES		#outside for, up to lines number
    move $t0, $zero     #outside for, t0 is index
	move $s2, $zero		#result
START:					#outside for
    bge $t0, $t7, ENDPRINT
	li $t6,	LETTERS_AMOUNT #inside for, up to characters in line
	move $t1, $zero		#inside for, t1 is index
	move $s1, $zero		#temporary = 0

START_COPYING:			#inside for
	bge $t1, $t6, ENDCOPY
	sll $s1, $s1, 1		#temporary *= 2
	move $t2, $s0		#t2 = &buff line
	addu $t2, $t2, $t1  #t2 = &(buff line + t1)
	la $t3, BUFFER		#t3 = &buff
	addu $t3, $t3, $t1  #t3 = &(buff + t1)
	li $t4, LETTERS_AMOUNT_BYTE #t4 = 12
	mul $t4, $t4, $t0	#t4 = 12 * t0
	addu $t3, $t3, $t4	#t3 = &(buff + t1 + 12*t0)
	move $t4, $zero
	lb $t4, ($t3)		#loads byte from t3 
	sb $t4, ($t2)		#stores byte from from load
operations: 
	addi $t1, $t1, 1	#t1 ++
if:	
	li $t2, L_B
	bne $t4, $t2, not_B
	addi $s1, $s1, 1	#temporary ++
	j not_R

not_B:
	li $t2, L_R
	bne $t4, $t2, not_R
	addi $s1, $s1, 1	#temporary ++

not_R:
	j START_COPYING

ENDCOPY:				#end inside for
	ble $s1, $s2, NOT_WORTH_IT #if temporary <= result: continue
	move $s2, $s1

NOT_WORTH_IT:
	addi $t0, $t0, 1	#t0 ++
	j START

ENDPRINT:				#end outside for
	li $v0, 1			# 1 --> print_int
	move $a0, $s2
	syscall

	li $v0, 10      		# End program
	syscall
