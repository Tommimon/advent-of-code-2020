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

def find_ends(riga, j):
    par = 0
    
    for start in range(j, 0, -1):
        start -= 1
        if (riga[start] == ')'):
            par += 1
        elif (riga[start] == '(' and par):
            par -= 1
        if(par == 0):
            break
    par = 0
    for end_ in range(j, len(riga)-1):
        end_ += 1
        if (riga[end_] == '('):
            par += 1
        elif (riga[end_] == ')' and par):
            par -= 1
        if(par == 0):
            break
    return(start-1, end_)


with open('./Gonduls/18/input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')
answer = 0
for riga in lista:
    neat_line = riga.replace(' ','')
    #I just need to add brackets for every '+' to change the order of operation
    for i in range(riga.count('+')):
        plus = -1
        j=0
        while(True):
            if (neat_line[j]=='+'):
                plus += 1
            #If i'm checking the correct +, I already added brackets for the + before so they don'y need more brackets
            if (plus==i):
                a, b = find_ends(neat_line, j)
                neat_line = neat_line[:a+1] + '(' +  neat_line[a+1:b+1]+ ')' +  neat_line[b+1:]
                break
            j += 1
    answer += in_brackets(neat_line)[0]
print(answer)