.data

.eqv DIM 44
.eqv BACKSLASH_N 10
.eqv zero 48

str1: .asciiz "Lettera: "
fileName: .asciiz "input.txt"
fileWords: .space DIM
car0: .asciiz "0"


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
	
	#Close the file
    	li $v0, 16         		# close_file syscall code
    	move $a0,$s0      		# file descriptor to close
    	syscall


        li $s0, DIM
        move $s1, $zero          #s1 is index
WHILE:  
        bge $s1, $s0, ENDWHILE
        la $t0, fileWords
        addu $t0, $t0, $s1
        li $v0, 4			# 4 --> print_string
	    la $a0, str1		# $a0 = address of null-terminated string to print    
	    syscall
        li $t1, BACKSLASH_N
        li $a0, 0                   #erase everything
        lb $a0, 0($t0)              #load byte only
        bne $a0, $t1, NOTN
        li $a0, zero
NOTN:
        li $v0, 11
        syscall                     #print char
        li $v0, 1
        syscall
        li $a0, BACKSLASH_N
        li $v0, 11
        syscall

        addi $s1, $s1, 1
        j WHILE
ENDWHILE:
        li $v0, 10      		# End program
	    syscall