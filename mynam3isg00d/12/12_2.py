#"When you think of rotations, always think of complex numbers" -some guy on reddit on day 1 2016 sol thread

pos = complex(0, 0)
way = complex(10, 1)
facing = complex(1, 0)

with open("mynam3isg00d/12/input.txt") as file:
    instructions = file.read().split('\n')
    for ins in instructions:
        action = ins[0]
        value = int(ins[1:])
        if action == 'N':
            way += 1j*value
        if action == 'S':
            way -= 1j*value
        if action == 'E':
            way += value
        if action == 'W':
            way -= value
        if action == 'L':
            way *= 1j**(value/90)
        if action == 'R':
            way /= 1j**(value/90)
        if action == 'F':
            pos += value*way
print(abs(pos.real) + abs(pos.imag))