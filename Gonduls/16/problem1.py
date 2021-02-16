with open('./Gonduls/16/input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')
rules = []
for index, el in enumerate(lista):
    if(el != ''):
        elem = el.replace('-', ' ').split(' ')
        rules.append([[int(elem[-5]), int(elem[-4])], [int(elem[-2]), int(elem[-1])]])
        continue
    break

index += 5
#index points to first line of nearby tickets
result = 0
for ticket in lista[index:]:
    fields = list(map(int, ticket.split(',')))
    for field in fields:
        #if field is not in range of any rules
        if(all(map(lambda rule: (not(rule[0][0]<=field<=rule[0][1]) and not(rule[1][0]<=field<=rule[1][1])), rules))):
            result += field
            break
print(result)