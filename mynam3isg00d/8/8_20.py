part1 = True
def blabla(lines):
    indxVisited = []
    indx = 0
    accumulator = 0
    while True:
        if indx in indxVisited:
            if part1:
                return accumulator
            return -1
        if indx >= len(lines):
            return accumulator
        line = lines[indx]
        indxVisited.append(indx)
        if "acc" in line:
            accumulator += int(line[3:])
            indx += 1
        elif "jmp" in line:
            indx += int(line[3:])
        elif "nop" in line:
            indx += 1

with open("mynam3isg00d/8/input.txt") as file:
    lines = file.read().split('\n')
    print("Part 1: " + str(blabla(lines)))
    part1 = False
    for i in range(len(lines)):
        if "nop" in lines[i]:
            lines[i] = lines[i].replace("nop", "jmp")
            if blabla(lines) == -1:
                lines[i] = lines[i].replace("jmp", "nop")
            else:
                print("Part 2: " + str(blabla(lines)))
                break
        if "jmp" in lines[i]:
            lines[i] = lines[i].replace("jmp", "nop")
            if blabla(lines) == -1:
                lines[i] = lines[i].replace("nop", "jmp")
            else:
                print("Part 2: " + str(blabla(lines)))
                break