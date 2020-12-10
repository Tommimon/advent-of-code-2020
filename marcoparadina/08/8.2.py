import re
arr=[]
with open('marcoparadina/8/input8.txt') as f:
        for line in f:
            curr_line=line.replace('\n', '').split(' ')
            curr_line.append(False) #tells if the instruction has already been executed
            arr.append(curr_line)

index=0
while index < len(arr):
    i = arr[index] 
    if i[0]=='jmp':
        i[0]='nop'
    elif i[0]=='nop':
        i[0]='jmp'
    
    repetition=False
    instruction_ID=0
    acc=0
    while instruction_ID < len(arr) and (repetition==False):
        values=arr[instruction_ID]
        if values[2]==True:                     
            repetition=True
        if values[0]=='acc':
            acc+=(int(values[1]))
            instruction_ID+=1
        elif values[0]=='jmp':
            instruction_ID+=(int(values[1]))
        elif values[0]=='nop':
            instruction_ID+=1
        values[2]=True
    final_acc=acc
    if repetition==True:        
        if i[0]=='jmp':
            i[0]='nop'
        elif i[0]=='nop':
            i[0]='jmp'
        for k in arr:
            k[2]=False 
        index+=1
    else:
        break
print('Solution to part 2:', final_acc)