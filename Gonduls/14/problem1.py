diz = {}
with open('input.txt', 'r') as inputf:
    for line in inputf.readlines():
        if ('mask' in line):
            rule = line[7:-1]
        else:
            #isolates needed value and converts it to a str of its binary transformation
            number = (str(bin(int(line.strip('\n').split(' ')[2])))[2:])
            #all 36 digits are needed for mask to work
            while(len(number)<36):
                number = '0' + number
            for i in range(len(rule)):
                if (rule[i] != 'X'):
                    number = number[:i] + rule[i] + number[i+1:]
            diz.update({line.split(']')[0][4:]: int(number, 2)})
print(sum(list(diz.values())))