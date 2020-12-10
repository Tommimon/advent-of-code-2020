import string
anyone_answered=0
everyone_answered=0
group=[]
check=[1]*(ord('z')-ord('a')+1)
with open('marcoparadina/6/input6.txt') as f:
    for line in f:
        if line == '\n':
            everyone_answered+=sum(check)
            check=[1]*(ord('z')-ord('a')+1)
            for letter in string.ascii_lowercase:
                if letter in group:
                    anyone_answered+=1
            group=[]
        else:
            group+=line
            for letter in (string.ascii_lowercase):
                    if letter not in line:
                        check[ord('a')-ord(letter)]=0
print('Solution to part :', anyone_answered)
print('Solution to part 2:', everyone_answered)