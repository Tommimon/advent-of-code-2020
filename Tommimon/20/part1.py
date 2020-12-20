def compare(string1, string2):
    return string1 == string2 or string1 == string2[::-1]


def alone(strings, ids):
    ris = []
    while len(strings) > 0:
        this = strings.pop()
        this_id = ids.pop()
        found = False
        for i, other in enumerate(strings):
            if compare(this, other):
                del strings[i]
                del ids[i]
                found = True
                break
        if not found:
            ris.append({'id': this_id, 'string': this})
    return ris


def get_row(tile, index):
    row = ""
    for i in tile:
        row += i[index]
    return row


with open('input.txt', 'r') as file:
    paragraph = file.read().split('\n\n')
tiles = []
for p in paragraph:
    lines = p.split('\n')
    newId = lines[0].strip('Tile ').strip(':')
    tiles.append({'id': int(newId), 'tile': lines[1:]})

borders = []
ids = []
for t in tiles:
    borders.append(t['tile'][0])
    borders.append(t['tile'][9])
    borders.append(get_row(t['tile'], 0))
    borders.append(get_row(t['tile'], 9))
    ids.append(t['id'])
    ids.append(t['id'])
    ids.append(t['id'])
    ids.append(t['id'])

unique = alone(borders, ids)
product = 1
for pos, u in enumerate(unique):
    for suc in unique[pos+1:]:
        if u['id'] == suc['id']:
            product *= u['id']
print(product)
