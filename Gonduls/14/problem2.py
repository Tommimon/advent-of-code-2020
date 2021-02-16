diz = {}
with open('./Gonduls/14/input.txt', 'r') as inputf:
    for line in inputf.readlines():
        if ('mask' in line):
            rule = line[7:-1]
        else:
            #isolates needed value and converts it to a str of its binary transformation
            number = (str(bin(int(line.split(' ')[0][4:-1])))[2:])
            #all 36 digits are needed for mask to work
            while(len(number)<36):
                number = '0' + number
            for i in range(len(rule)):
                if (rule[i] != '0'):
                    number = number[:i] + rule[i] + number[i+1:]

            #This for creates all 2^X combinations through i
            for i in range(2**number.count('X')):
                X_values = str(bin(i))[2:]

                #this while makes sure that x_values contains right amount of values for the replace part
                while(len(X_values) < number.count('X')):
                    X_values = '0' + X_values

                #replace part: calculates address by replacing x value with first x ('X', value, ->1<-) encountered
                address = number
                for value in X_values:
                    address = address.replace('X', value, 1)
                diz.update({address: int(line.strip('\n').split(' ')[2])})
print(sum(list(diz.values())))