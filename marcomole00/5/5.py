#i'm an idiot, this algoritm is fucking useless, the FB and LR notation is literally binary notation. 
def ticketCheck(line):
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7
    for i in range (7):
        if line[i] == 'F':
            rowMax = rowMin + abs(int((rowMax - rowMin)/2))
        else: rowMin =  rowMax - abs(int((rowMax - rowMin)/2))
    for i in range(3):
        if line[7+i] == 'L':
            colMax = colMin + abs(int((colMax - colMin)/2))
        else: colMin =  colMax - abs(int((colMax - colMin)/2))
    ID = rowMax*8 + colMax
    return(rowMax, colMax,ID)
        

iDs=[]

with open('marcomole00/5/input.txt') as f:
    for line in f:
        line = line.strip('\n')
        tempRow,tempCol, tempId = ticketCheck(line)
        
        iDs.append( tempId)

    
    iDs.sort()
    for i in range(len(iDs)):
        if  (iDs[i+1] - iDs[i])==2 and ((iDs[i] +1 ) not in iDs):  #at the end the index goes out of range but really who cares
            print('my ID is :', iDs[i]+1)
        
    print(max(iDs))
    
        

