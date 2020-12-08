indexPassed = []
globalAcc = 0
with open('marcomole00/8/input.txt') as file:
    lines = file.read().split('\n')
    for instruction in lines:
        
        indexIn = 0
        extIndex = lines.index(instruction)
        indexPassed = []
        infiniteLoop = False
        accumulator = 0
        field, value = instruction.split(' ')
        if field == 'nop': 
            lines[extIndex]=  instruction.replace('nop', 'jmp')
        elif field == 'jmp': 
            lines[extIndex] =  instruction.replace('jmp','nop')

        while True:
            indexPassed.append(indexIn)
            fieldTemp, valueTemp = lines[indexIn].split(' ')
            print (lines[extIndex], '  ', fieldTemp)
            if fieldTemp == 'jmp':
                indexIn += int(valueTemp)
            else: indexIn += 1
            if fieldTemp == 'acc':
                 accumulator += int(valueTemp)
            if indexIn in indexPassed:
                #print(instruction, '   ', fieldTemp)
                infiniteLoop = True
                break
            if(indexIn >= len(lines)):
                print(accumulator)
                break
        if infiniteLoop == True:
            if field == 'nop': 
                lines[extIndex] = instruction
            elif field == 'jmp': 
                lines[extIndex] =  instruction
        else: break

print(accumulator)