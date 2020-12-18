def evaluate(string, is_part2):
    expression = []
    i = 0
    while i < len(string):
        if string[i] != '(':
            expression.append(string[i])
        else:
            block = ''
            layer = 1
            while layer > 0:
                i += 1
                block += string[i]
                if string[i] == '(':
                    layer += 1
                elif string[i] == ')':
                    layer -= 1
            expression.append(evaluate(block[:-1], is_part2))
        i += 1
    while len(expression) > 1:
        if is_part2 and '+' in expression:
            pos = expression.index('+')
            if pos == -1:  # if no '+' start from first '*'
                pos = 1
        else:
            pos = 1
        if expression[pos] == '+':
            expression[pos-1] = int(expression[pos-1]) + int(expression[pos+1])
        if expression[pos] == '*':
            expression[pos-1] = int(expression[pos-1]) * int(expression[pos+1])
        del expression[pos+1]
        del expression[pos]
    return expression[0]


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
total = 0
for line in lines:
    total += evaluate(line.replace(' ', ''), False)
print(total)
total = 0
for line in lines:
    total += evaluate(line.replace(' ', ''), True)
print(total)
