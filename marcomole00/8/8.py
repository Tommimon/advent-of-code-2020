indexPassed = set()
accumulator = 0

with open('marcomole00/8/input.txt') as file:
    lines = file.read().split('\n')
    index = 0 
    while lines[index] != '\n':
        indexPassed.add(index)
        istr , value = lines[index].split(' ')
        if istr == 'jmp':
            index += int(value)
        else: index += 1
        if istr == 'acc': accumulator += int(value)
        
        if index in indexPassed : 
            break          
print(accumulator)


    