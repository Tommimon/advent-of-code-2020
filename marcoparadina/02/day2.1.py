with open('marcoparadina/2/input_d2.txt') as f:
    i=0
    inf_arr=[]
    sup_arr=[]
    sol_part1=0
    sol_part2=0
    input_arr=[]
    for line in f:
        for word in line.split():
            input_arr.append(word)        #input file entirely converted in array: every group of 3 consecutive elements is a line of the original input
    
    while i < len(input_arr):  
        ###############setting of superior and inferior limit for character frequency############
        el=input_arr[i]
        separation_flag=0
        
        del inf_arr[:]
        del sup_arr[:]           
        for char in el:
            if char == '-':
                separation_flag = 1
                
            elif separation_flag==0:
                inf_arr.append(int(char))
            elif separation_flag==1:
                sup_arr.append(int(char))

        ####################INF########################       
        if len(inf_arr)==2:         #sta parte è inguardabile va sistemata
            inf_arr[0]=inf_arr[0]*10
            inf=inf_arr[0]+inf_arr[1]
        else :
            inf=inf_arr[0]      

        ####################SUP########################
        if len(sup_arr)==2:
            sup_arr[0]=sup_arr[0]*10
            sup=sup_arr[0]+sup_arr[1]
        else :
            sup=sup_arr[0]   

        ################setting the current character#########################
        i=i+1
        el=input_arr[i]
        curr_char=el[0]
        
        ################looks for curr_char in the password###################
        i=i+1
        el=input_arr[i]
        freq=0
        for c in el:
            if c==curr_char:
                freq=freq+1
        # I don't know why, i shouldn't wonder why, i do not want to know why, 
        # but the logical operators '&' doesn't work so I find myself forced to do this horribleness.
        if inf<=freq:
            if sup>=freq:
                sol_part1+=1
        ##################################part2###############################################
        flag=0
        if len(el)>=(sup):
            if (el[sup-1]==curr_char) ^ (el[inf-1]==curr_char):
                flag=1
                
        elif len(el)<(sup):
            if len(el)>=(inf):
                if el[inf-1]==curr_char:
                    flag=1

        sol_part2+=flag
        i=i+1
    print('part1 solution:', sol_part1)
    print('part2 solution:', sol_part2)