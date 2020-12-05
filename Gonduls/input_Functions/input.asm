	.text
	.globl main
	
main:
	#HOW TO READ INTO A FILE
	
	li $v0,13           	# open_file syscall code = 13
    	la $a0,fileName     	# get the file name
    	li $a1,0           	# file flag = read (0)
    	syscall
    	move $s0,$v0        	# save the file descriptor. $s0 = file
	
	#read the file
	li $v0, 14		# read_file syscall code = 14
	move $a0,$s0		# file descriptor
	la $a1,fileWords  	# The buffer that holds the string of the WHOLE file
	la $a2,1024		# hardcoded buffer length
	syscall
	
	# print whats in the file
	li $v0, 4		# read_string syscall code = 4
	la $a0,fileWords
	syscall
	
	#Close the file
    	li $v0, 16         		# close_file syscall code
    	move $a0,$s0      		# file descriptor to close
    	syscall
    	
    #	# HOW TO WRITE INTO A FILE
    #	
    #	#open file 
    #	li $v0,13           	# open_file syscall code = 13
    #	la $a0,fileName     	# get the file name
    #	li $a1,1           	# file flag = write (1)
    #	syscall
    #	move $s1,$v0        	# save the file descriptor. $s0 = file
    #	
    #	#Write the file
    #	li $v0,15		# write_file syscall code = 15
    #	move $a0,$s1		# file descriptor
    #	la $a1,toWrite		# the string that will be written
    #	la $a2,21		# length of the toWrite string
    #	syscall
    #	
	##MUST CLOSE FILE IN ORDER TO UPDATE THE FILE
    #	li $v0,16         		# close_file syscall code
    #	move $a0,$s1      		# file descriptor to close
    #	syscall

#STRINGS
.data
toWrite: .asciiz "Hello World was here"
fileName: .asciiz "appunti.txt"
fileWords: .space 1024




################################# Copied from Riccardo ################################ (+/-) ######################



.data

.eqv FILE_MAX_SIZE 9382		# used to set buffer size for reading	
.eqv LETTERS_AMOUNT 10
.eqv LETTERS_AMOUNT_BYTE 12	# add 2: "\n" and misterious char
.eqv LINES 782
.eqv L_F 70
.eqv L_B 66
.eqv L_L 75
.eqv L_R 82

BUFFER: .space FILE_MAX_SIZE
BUFFER_LINE: .asciiz "0000000000\n"
FILE_NAME: .asciiz "input.txt"
END: .asciiz "\n"
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