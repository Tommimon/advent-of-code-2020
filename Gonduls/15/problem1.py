numbers = {}
with open('input.txt', 'r') as inputf:
    lista = inputf.read().split(',')
    for i, el in enumerate(lista):
        numbers.update({int(el): i+1})
end =  2020#change to 30000000 for problem 2 
curr = 0
i += 2
while(i<end):
    if (curr in numbers.keys()):
        next_ = i - numbers[curr]
        numbers[curr] = i
        curr = next_
    else:
        numbers.update({curr: i})
        curr  = 0
    i += 1
print(curr)