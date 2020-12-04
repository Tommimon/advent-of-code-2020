with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()

def conditions(elem):
    if(not(len(elem.split(' '))==9 or (len(elem.split(' '))==8 and not ('cid' in elem)))):
        return 0
    elem = elem[:-1].split(' ')
    for info in elem:
        if (info[:3] == 'byr' and (len(info[4:])!=4 or (int(info[4:])<1920) or (int(info[4:])>2002))):
            print(str(elem)+' 0')
            return 0
        if (info[:3] == 'iyr' and (len(info[4:])!=4 or (int(info[4:])<2010) or (int(info[4:])>2020))):
            print(str(elem)+' 1')
            return 0
        if (info[:3] == 'eyr' and (len(info[4:])!=4 or (int(info[4:])<2020) or (int(info[4:])>2030))):
            print(str(elem)+' 2')
            return 0
        if (info[:3] == 'pid' and (len(info[4:])!=9 or (not (info[4:].isdecimal())))):
            print(str(elem)+' 3')
            return 0
        if (info[:3] == 'ecl' and (len(info[4:])!=3 or (not (info[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])))):
            print(str(elem)+' 4')
            return 0
        if (info[:3] == 'hcl' and (len(info[4:])!=7 or info[5] != '#')):
            try:
                int(info[5:], 16)
            print(str(elem)+' 4')
            return 0
    return 1

lista = ['']
for element in inlist:
    if (element == '\n'):
        lista.append('')
        continue
    lista[-1]=lista[-1]+element[:-1]+' '


ris=0
for element in lista:
    if (conditions(element)):
       ris += 1
print (ris)