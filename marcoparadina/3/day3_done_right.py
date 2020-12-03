def set_go(line_count): # makes the move down when move_down is 2
    go=1
    if (line_count % 2)!=0:
        go=0
    return go

def expansion_factor(move_right, move_down, file_len):  #how much to expand every line of the input to obtain the complete map
    i=file_len/move_down
    j=i*move_right
    return int(j)   

def file_length(file_name): #computes the length of a file in a single function in order to make it faster (sligthly)
    with open(file_name) as f:
        count=0
        for line in f:
            count+=1
    return count   

def slope_check(move_right,move_down, file_name, file_len):
    exp=expansion_factor(move_right, move_down, file_len)
    with open(file_name) as f:
        position=0
        trees=0
        line_count=0
        go=1
        for line in f:   
            if(move_down==2):
                go=set_go(line_count)   
            if go==1: 
                arr=[]
                for k in range(exp):
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

file_len=file_length('marcoparadina/3/input_d3.txt')
a=slope_check(1,1,'marcoparadina/3/input_d3.txt', file_len)    
b=slope_check(3,1,'marcoparadina/3/input_d3.txt', file_len)
c=slope_check(5,1,'marcoparadina/3/input_d3.txt', file_len)
d=slope_check(7,1,'marcoparadina/3/input_d3.txt', file_len)
e=slope_check(1,2,'marcoparadina/3/input_d3.txt', file_len)
print('result:', a*b*c*d*e)    