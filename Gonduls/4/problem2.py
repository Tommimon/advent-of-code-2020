with open('input.txt', 'r') as inputf:
    inlist = inputf.readlines()

def conditions(elem):
    if(not(len(elem.split(' '))==9 or (len(elem.split(' '))==8 and not ('cid' in elem)))):
        return 0
    elem = elem[:-1].split(' ')
    for info in elem:
        if (info[:3] == byr and (len(info[4:])!=4 or (int(info[4:])<1920) or (int(info[4:])>2020)))
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