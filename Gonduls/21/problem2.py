with open('./Gonduls/21/input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')

# first selection of ingredients containing allergens
all_ingredients = []
allergens = {}
for line in lista:
    allergens_list = (line.split(' (contains ')[1].replace(')','')).split(', ')
    ingredients_list = (line.split(' (contains ')[0].replace(')','')).split(' ')
    for ingredient in ingredients_list:
        all_ingredients.append(ingredient)
    for allergen in allergens_list:
        if allergen in allergens.keys():
            new_ingredients = []
            for ingredient in ingredients_list:
                if ingredient in allergens[allergen]:
                    new_ingredients.append(ingredient)
            allergens[allergen] = new_ingredients
        else:
            allergens[allergen] = ingredients_list

# second selection of ingredients containing allergens (check if an allergen has more than one ingredient that can contain it)
while any(list(map(lambda el: len(el)>1, list(allergens.values())))):
    for allergen in allergens.keys():
        if len(allergens[allergen])>1:
            continue
        ingredient = allergens[allergen][0]
        for culprit_allergen in allergens.keys():
            if len(allergens[culprit_allergen])>1 and ingredient in allergens[culprit_allergen]:
                allergens[culprit_allergen].remove(ingredient)

aller = list(allergens.keys())
aller.sort()
ingr = [ingredient[0] for ingredient in [allergens[allergen] for allergen in aller]]
print(','.join(ingr))