with open('input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')
rules = []
for index, el in enumerate(lista):
    if(el != ''):
        elem = el.replace('departure ','departure_',).replace('arrival ','arrival_',).replace('-', ' ').split(' ')
        rules.append([[int(elem[-5]), int(elem[-4])], [int(elem[-2]), int(elem[-1])], elem[0][:-1]])
        continue
    break

index += 5
valid_list = []
#index points to first line of nearby tickets
for ticket in lista[index:]:
    fields = list(map(int, ticket.split(',')))
    valid = True
    for field in fields:
        #if field is not in range of any rule
        if(all(map(lambda rule: (not(rule[0][0]<=field<=rule[0][1]) and not(rule[1][0]<=field<=rule[1][1])), rules))):
            valid = False
            break
    if(valid):
        valid_list.append(fields)
#creates list of possible position inside a ticket for each rule
rules_positions = []
for rule in rules:
    rules_positions.append([])
    for i in range(len(fields)):
        if all(map(lambda ticket: ((rule[0][0]<=ticket[i]<=rule[0][1]) or (rule[1][0]<=ticket[i]<=rule[1][1])), valid_list)):
            rules_positions[-1].append(i)
#eliminates impossible positions that other rules have already taken
while (any(map(lambda el: len(el)!=1, rules_positions))):
    for j in range(len(rules_positions)):
        if (len(rules_positions[j])==1):
            to_remove = rules_positions[j][0]
            for ind, elem in enumerate(rules_positions):
                if(len(elem)!=1 and to_remove in elem):
                    rules_positions[ind].remove(to_remove)
#calculates result
result = 1
my_ticket = list(map(int, lista[lista.index('your ticket:')+1].split(',')))
for index in rules_positions[:6]:
    result *= my_ticket[index[0]]
print(result)
