def set_go(line_count): # makes the move down when movve_down is 2
    go=1
    if (line_count % 2)!=0:
        go=0
    return go
def slope_check(move_right,move_down):    
    with open('marcoparadina/3/input_d3.txt') as f:
        position=0
        trees=0
        line_count=0
        go=1
        for line in f:   
            if(move_down==2):
                go=set_go(line_count)   
            if go==1: 
                arr=[]
                for k in range(80):
                    arr+=line
                for x in arr:
                # When i concatenate too many lines in a single string an '\n' is automatically added 
                # between some of them for reasons i'm not familiar with. This for cycle removes them 
                # in order not to corrupt the counting of the trees.
                    if x=='\n': 
                        arr.remove(x)
                if arr[position]=='#':
                    trees+=1
                position+=move_right
            line_count+=1
            go=1
    return trees    
print('result:', slope_check(1,1)*slope_check(3,1)*slope_check(5,1)*slope_check(7,1)*slope_check(1,2))    