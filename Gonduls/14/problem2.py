diz = {}
with open('input.txt', 'r') as inputf:
    for line in inputf.readlines():
        if ('mask' in line):
            rule = line[7:-1]
        else:
            number = (str(bin(int(line.strip('\n').split(' ')[2])))[2:])
            while(len(number)<36):
                number = '0' + number
            for i in range(len(rule)):
                if (rule[i] != 'X'):
                    number = number[:i] + rule[i] + number[i+1:]
            diz.update({line.split(']')[0][4:]: int(number, 2)})
print(sum(list(diz.values())))