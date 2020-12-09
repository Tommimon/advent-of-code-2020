import re
arr=[]
acc=0
with open('marcoparadina/8/input8.txt') as f:
    for line in f:
        curr_line=line.replace('\n', '').split(' ')
        curr_line.append(False) #tells if the instruction has already been executed
        arr.append(curr_line)   
    
    instruction_ID=0

    while instruction_ID < len(arr):
        values=arr[instruction_ID]
        if values[2]==True:
            final_acc=acc
            print('Solution to part 1:', final_acc)
            repetition=True
            break
        if values[0]=='acc':
            acc+=(int(values[1]))
            instruction_ID+=1
        elif values[0]=='jmp':
            instruction_ID+=(int(values[1]))
        elif values[0]=='nop':
            instruction_ID+=1
        values[2]=True
        