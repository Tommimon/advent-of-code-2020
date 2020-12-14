def updateMemory(mask, memAss):
    bitreplace = mask.replace('1','0').replace('X','1') #1 if X, 0 if set value
    bitreplace = int(bitreplace, 2)
    mask = mask.replace('X','0')                      #1/0 if set value, 0 if X
    mask = int(mask, 2)
    for inst in memAss:
        place, value = inst.split(' = ')
        value = int(value)
        value = value & bitreplace
        value = value + mask
        mem[int(place)] = value
        
mem = [0]*100000
with open("input.txt") as file:
    infos = file.read().replace('mask = ','\n').strip('\n').replace('mem[','').replace(']','').split('\n\n')
    for info in infos:
        lines = info.split('\n')
        mask = lines[0]
        memAss = lines[1:]
        updateMemory(mask, memAss)

print(sum(mem))