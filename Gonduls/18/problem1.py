def in_brackets(riga, i=0):
    answer = 0
    operation = '+'
    while(i<len(riga)):
        if(riga[i] == '('):
            brackets, i = in_brackets(riga, i+1)
            if (operation == '+'):
                answer += brackets
            if (operation == '*'):
                answer *= brackets
        elif (riga[i] in ['+','*']):
            operation = riga[i]
        elif(riga[i] == ')'):
            return(answer, i)
        else:
            if (operation == '+'):
                answer += int(riga[i])
            if (operation == '*'):
                answer *= int(riga[i])
        i += 1
    return(answer, i)


with open('input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')
answer = 0
for riga in lista:
    answer += in_brackets(riga.replace(' ',''))[0]
print(answer)