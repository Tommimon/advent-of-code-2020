def replace_el(key):
    if ('a' in rules[key][0] or 'b' in rules[key][0]):
        return rules[key]
    lists = []
    answers = []
    for i, option in enumerate(rules[key]):
        lists.append([])
        for index, part in enumerate(option.split(' ')):
            lists[i].append(replace_el(part))
        if len(lists[i]) == 2:
            for first_part in lists[i][0]:
                for second_part in lists[i][1]:
                    answers.append(first_part + second_part)
        else:
            for j in range(len(lists[i][0])):
                answers.append(lists[i][0][j])

    rules[key]= answers
    return answers

with open('./Gonduls/19/input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')

rules = {}
for i, riga in enumerate(lista):
    if riga == '':
        break
    rules[riga.split(': ')[0]] = riga.split(': ')[1].replace('"','').split(' | ')

lenght42 = 10000
answers42 = replace_el('42')
for el in answers42 :
    lenght42 = min(lenght42, len(el))

lenght31 = 10000
answers31 = replace_el('31')
for el in answers31 :
    lenght31 = min(lenght31, len(el))

plausible = []
i+=1
zero_ans = replace_el('0')
result = 0
while(i<len(lista)):
    if lista[i] in zero_ans:
        result += 1
    elif lista[i][:lenght42] in rules['42'] and lista[i][-lenght31:] in rules['31']:
        plausible.append(lista[i])
    i += 1

for el in plausible:
    #if el respects rules 11 and 8 (looped) then it has to end with N*(element in rule 31) 
    #and start with M*(element in rule 42), where M>N>=1 to respect both rules
    while el[-lenght31:] in rules['31'] and el[:lenght42] in rules['42'] and len(el)>= lenght31+lenght42:
        el = el[lenght42:-lenght31]
    if len(el)==0:
        continue
    while el[:lenght42] in rules['42']:
        el = el[lenght42:]
    if len(el)== 0:
        result += 1

print(result)