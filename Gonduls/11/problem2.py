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
            letters = seen (matrix, [j,i])
            if(letters.count('#')==0):
                result[-1] = result[-1] + '#'
            elif(letters.count('#')>4):
                result[-1] = result[-1] + 'L'
            else:
                result[-1] = result[-1] + el
    return result[:]

def seen(matrix, coordinates):
    directions = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    ris =''
    for elem in directions:
        point = [coordinates[0]+elem[0],coordinates[1]+elem[1]]
        while (len(matrix[0])>point[1] >=0 and len(matrix)>point[0]>=0):
            if (matrix[point[0]][point[1]] != '.'):
                ris = ris + matrix[point[0]][point[1]]
                break
            point = [point[0]+elem[0],point[1]+elem[1]]
    return ris

while(True):
    newlista = change(lista[:])
    if(newlista == lista):
        break
    lista = newlista
ris = sum(list(map(lambda el: el.count('#') , lista)))
print(ris)