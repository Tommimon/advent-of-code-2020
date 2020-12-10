def run_code(instructions):
    pos = 0
    counter = 0
    while True:
        if pos == len(instructions):
            print(counter)
            ris = counter
            break
        if 'end' in instructions[pos][0]:
            ris = counter
            break
        instructions[pos][0] = instructions[pos][0] + 'end'
        if instructions[pos][0] == 'accend':
            counter += int(instructions[pos][1])
        elif instructions[pos][0] == 'jmpend':
            pos += int(instructions[pos][1]) - 1
        pos += 1
    for j in range(len(instructions)):
        if 'end' in instructions[j][0]:
            instructions[j][0] = instructions[j][0][0:3]
    return ris


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
print(run_code(lines))
for i in range(len(lines)):
    if lines[i][0] == 'jmp':
        lines[i][0] = 'nop'
        run_code(lines)
        lines[i][0] = 'jmp'
    elif lines[i][0] == 'nop':
        lines[i][0] = 'jmp'
        run_code(lines)
        lines[i][0] = 'nop'
