import string #using string.hexdigits in: all(c in string.hexdigits for c in string), returns boolean
with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()
    inlist[-1]=inlist[-1] + ' '   #space needed for preservation of all letters

def conditions(elem): #checks if it's aight, returns 0 if not
    if(not(len(elem.split(' '))==9 or (len(elem.split(' '))==8 and not ('cid' in elem)))):
        return 0
    elem = elem[:-1].split(' ')
    for info in elem:
        if (info[:3] == 'byr' and (len(info[4:])!=4 or (int(info[4:])<1920) or (int(info[4:])>2002))):
            return 0
        if (info[:3] == 'iyr' and (len(info[4:])!=4 or (int(info[4:])<2010) or (int(info[4:])>2020))):
            return 0
        if (info[:3] == 'eyr' and (len(info[4:])!=4 or (int(info[4:])<2020) or (int(info[4:])>2030))):
            return 0
        if (info[:3] == 'pid' and (len(info[4:])!=9 or (not (info[4:].isdecimal())))):
            return 0
        if (info[:3] == 'ecl' and (len(info[4:])!=3 or (not (info[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])))):
            return 0 #I'm truly for this condition, it wad either this way or a more complicated one. You're lucky I didn't do all conditions in a line altogether
        if (info[:3] == 'hcl' and (len(info[4:])!=7 or info[4] != '#' or not all(c in string.hexdigits for c in info[5:]))):
            return 0
        if (info[:3] == 'hgt' and ((info[-2:]== 'cm' and (int(info[4:-2])<150 or int(info[4:-2])>193)) or (info[-2:]== 'in' and (int(info[4:-2])<59 or int(info[4:-2])>76)) or (info[-2:]!= 'cm' and info[-2:]!= 'in'))):
            return 0 #This one's even worse, not my fault really. Elseifs would have done an even worse job
    return 1

lista = ['']
for element in inlist:
    if (element == '\n'):
        lista.append('')
        continue
    lista[-1]=lista[-1]+element[:-1]+' '

ris=0
for element in lista:
    ris += conditions(element)
print (ris)