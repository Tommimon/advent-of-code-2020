with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
foods = list(map(lambda e: {
    'ingredients': e.split(' (contains ')[0].split(' '),
    'allergens': e.split(' (contains ')[1][:-1].split(', ')
}, lines))
# print(''.join(list(map(lambda e: str(e) + '\n', foods))))

allergens = set()
ingredients = set()
for f in foods:
    allergens = allergens.union(set(f['allergens']))
    ingredients = ingredients.union(set(f['ingredients']))

notPossible = ingredients.copy()
for a in allergens:  # search possible ingredients
    newPossible = set()
    for f in foods:
        if a in f['allergens']:
            if len(newPossible) == 0:
                newPossible = set(f['ingredients'])  # set an initial value for newPossible
            else:
                newPossible = newPossible.intersection(set(f['ingredients']))
    notPossible = notPossible.difference(newPossible)

counter = 0
for f in foods:  # count not possible ingredients occurrence
    for n in notPossible:
        if n in f['ingredients']:
            counter += 1
print(counter)

possible = ingredients.difference(notPossible)
matchList = []
# continue if there are possible ingredients left because when I find the allergen related to an ingredient
# I remove that ingredient from possible list
while len(possible) > 0:
    for a in allergens:
        matching = possible.copy()
        for f in foods:
            if a in f['allergens']:
                matching = matching.intersection(set(f['ingredients']))
        # if there are more than one matching ingredient do nothing eventually all other ingredients will find their
        # allergen and will be removed from possible and only the correct one will remain
        if len(matching) == 1:
            possible.remove(list(matching)[0])
            matchList.append((a, list(matching)[0]))
matchList.sort(key=lambda e: e[0])
canonical = ''.join(list(map(lambda e: str(e[1]) + ',', matchList)))[:-1]
print(canonical)
