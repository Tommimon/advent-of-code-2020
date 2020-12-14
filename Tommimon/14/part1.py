with open('input.txt', 'r') as file:
    memory = [0]
    mask = ""
    for fullLine in file.readlines():
        command = fullLine.strip('\n').replace(']', '').replace('[', ' = ').split(' = ')
        if command[0] == 'mask':
            mask = command[1]
        elif command[0] == 'mem':
            val = bin(int(command[2]))[2:]
            ris = ""
            for i in range(0, len(mask)):
                if mask[len(mask) - 1 - i] == 'X':
                    if i < len(val):
                        ris += val[len(val) - 1 - i]
                    else:
                        ris += '0'
                else:
                    ris += mask[len(mask) - 1 - i]
            pos = int(command[1])
            if pos >= len(memory):
                memory += [0] * (pos - len(memory) + 1)
            memory[pos] = int(ris[::-1], 2)
print(sum(memory))
