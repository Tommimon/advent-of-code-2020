import string
with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()

result = 0
i=0
inlist.append('\n') #needed for last group to check
for j in range(len(inlist)):
    if (inlist[j] == '\n'):
        for letter in string.ascii_lowercase:
            result += letter in (''.join(inlist[i:j]))
        i=j+1

print(result)