indexPassed = set()
accumulator = 0
firstPass = True
istrSet = []
#first part
with open('marcomole00/8/test.txt') as file:
    lines = file.read().split('\n')
    index = 0 
    while lines[index] != '\n':
        indexPassed.add(index)
        istr , value = lines[index].split(' ')
        
        
        
        if istr == 'jmp':
            index += int(value)
        else: index += 1
        if istr == 'acc': accumulator += int(value)
        
        if index in indexPassed and firstPass == True: # this is already the next expression which has not been fetched
            if firstPass == True:
                print(accumulator)
                firstPass = False
            if istr == 'nop':
                lines[index] = lines[index].replace('nop', 'jmp')
                index = index -1
                print('change nop to jmp')
            elif istr == 'jmp':
                index = index - int(value)
                lines[index] = lines[index].replace('nop', 'jmp')
                print('change jmp to nop , index = ', index )
        print(index)
            
print(accumulator)


    