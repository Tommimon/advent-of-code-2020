#recursive function, swaps evey value in dictionary for a list of possible combinations
def replace_el(key):
    #bad way of checking if a value has already been found for a specific key. Effective tho.
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

#input phase
with open('input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')

#program start
rules = {}
for i, riga in enumerate(lista):
    if riga == '':
        break
    rules[riga.split(': ')[0]] = riga.split(': ')[1].replace('"','').split(' | ')

i+=1
zero_ans = replace_el('0')

result = 0
while(i<len(lista)):
    if lista[i] in zero_ans:
        result += 1
    i += 1
print(result)