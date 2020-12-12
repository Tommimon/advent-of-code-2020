#"When you think of rotations, always think of complex numbers" -some guy on reddit on day 1 2016 sol thread

pos = complex(0, 0)
facing = complex(1, 0)

with open("mynam3isg00d/12/input.txt") as file:
    instructions = file.read().split('\n')
    for ins in instructions:
        action = ins[0]
        value = int(ins[1:])
        if action == 'N':
            pos += 1j*value
        if action == 'S':
            pos -= 1j*value
        if action == 'E':
            pos += value
        if action == 'W':
            pos -= value
        if action == 'L':
            facing *= 1j**(value/90)
        if action == 'R':
            facing /= 1j**(value/90)
        if action == 'F':
            pos += facing*value
print(abs(pos.real) + abs(pos.imag))