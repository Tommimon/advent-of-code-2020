import string
with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()

result = 0
i=0                 #group index, always 0 or ('\n' index +1)
inlist.append('\n') #needed for last group to check
for j in range(len(inlist)):
    if (inlist[j] == '\n'):
        for letter in string.ascii_lowercase:
            result += (''.join(inlist[i:j])).count(letter) == (j-i)
        i=j+1

print(result)