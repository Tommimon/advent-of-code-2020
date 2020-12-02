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