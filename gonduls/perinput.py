with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()
    for element in inlist:
        inlist[inlist.index(element)]=int(element)
    print(inlist)