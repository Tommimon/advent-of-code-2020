with open('./Gonduls/11/input.txt', 'r') as inputf:
        lista= list(inputf.read().split('\n'))

def change(matrix):
    result = []
    for j,line in enumerate(matrix):
        result.append('')
        for i, el in enumerate(line):
            if(el == '.'):
                result[-1] = result[-1] + '.'
                continue
            adjacent = [[j-1,i-1],[j-1,i],[j-1,i+1],[j+1,i-1],[j+1,i],[j+1,i+1],[j,i-1],[j,i+1]]
            letters = []
            for direction in adjacent:
                if (len(line)>direction[1] >=0 and len(matrix)>direction[0]>=0):
                    letters.append(matrix[direction[0]][direction[1]])
            if(letters.count('#')==0):
                result[-1] = result[-1] + '#'
            elif(letters.count('#')>3):
                result[-1] = result[-1] + 'L'
            else:
                result[-1] = result[-1] + el
    return result[:]

while(True):
    newlista = change(lista[:])
    if(newlista == lista):
        break
    lista = newlista
ris = sum(list(map(lambda el: el.count('#') , lista)))
print(ris)