import math


def compare(string1, string2):
    return string1 == string2 or string1 == string2[::-1]


def borders(tile):
    return [get_col(tile, 0), tile[0][::-1], get_col(tile, 9)[::-1], tile[9]]  # clockwise


def alone(strings, ids):
    ris_id = []
    ris_string = []
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
            ris_id.append(this_id)
            ris_string.append(this)
    return ris_id, ris_string


def get_col(tile, c):
    r = ""
    for i in tile:
        r += i[c]
    return r


def match(b1, tile2):
    borders2 = borders(tile2)
    for i, b2 in enumerate(borders2):
        if b1 == b2:
            return i, False,
        elif b1 == b2[::-1]:
            return i, True,
    return None, None


def flip_tile(tile, must_flip=True):
    if must_flip:
        return tile[::-1]
    return tile


def rot90(tile, length=10):
    new_tile = [None] * length
    for j in range(length):
        string = ""
        for i in range(length):
            string += tile[i][j]
        new_tile[length - j - 1] = string
    return new_tile


def rot_tile(tile, n, length=10):
    for i in range(n):
        tile = rot90(tile, length)
    return tile


def draw(tile, pattern):
    result = 0
    for y in range(len(tile) - len(pattern)):
        for x in range(len(tile[0]) - len(pattern[0])):
            correct = True
            new_covered = 0
            for i in range(len(pattern)):
                for j in range(len(pattern[0])):
                    if pattern[i][j] == '#':
                        if tile[y + i][x + j] == '#':
                            new_covered += 1
                        else:
                            correct = False
            if correct:
                result += new_covered
    return result


with open('input.txt', 'r') as file:
    tiles = dict()
    for p in file.read().split('\n\n'):
        lines = p.split('\n')
        tiles[int(lines[0].strip('Tile ').strip(':'))] = lines[1:]
size = int(math.sqrt(len(tiles)))

borderStrings = []
borderIds = []
for key, t in tiles.items():
    borderStrings += borders(t)
    borderIds += [key] * 4
idsAlone, stringsAlone = alone(borderStrings, borderIds)  # strings without match and respective ids
corner = None
product = 1
for index, a in enumerate(idsAlone):
    for suc in idsAlone[index + 1:]:
        if a == suc:
            corner = a
            product *= a
print(product)

rotation = None
for index, b in enumerate(borders(tiles[corner])):  # find rotation of first corner
    if b in stringsAlone:
        if not(index == 3 and rotation == 0):
            rotation = index
rotation = (rotation - 1) % 4
photo = [[{'id': corner, 'tile': rot_tile(tiles[corner], rotation)}]]
for stepRow in range(size):
    if stepRow != 0:
        for key, t in tiles.items():  # add new row and first tile of this row
            if key != photo[stepRow - 1][0]['id']:
                rot, flip = match(photo[stepRow - 1][0]['tile'][9][::-1], t)
                if rot is not None:
                    photo.append([{'id': key, 'tile': rot_tile(flip_tile(rot_tile(t, rot), flip), 3)}])
                    break
    for stepCol in range(size - 1):
        for key, t in tiles.items():  # add next tile to row
            if key != photo[stepRow][stepCol]['id']:
                rot, flip = match(get_col(photo[stepRow][stepCol]['tile'], 9), t)
                if rot is not None:
                    photo[stepRow].append({'id': key, 'tile': flip_tile(rot_tile(t, rot), flip)})
                    break

for row in range(size):  # remove border
    for col in range(size):
        photo[row][col]['tile'] = photo[row][col]['tile'][1:-1]
        for line in range(8):
            photo[row][col]['tile'][line] = photo[row][col]['tile'][line][1:-1]

fullPhoto = []
for row in range(size):  # concat tiles to create photo
    for line in range(8):
        fullLine = ""
        for col in range(size):
            fullLine += photo[row][col]['tile'][line]
        fullPhoto.append(fullLine)

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

covered = 0
for rot in range(4):  # count '#' covered from a monster
    covered += draw(rot_tile(fullPhoto, rot, 8 * size), monster)
    covered += draw(flip_tile(rot_tile(fullPhoto, rot, 8 * size)), monster)

total = 0
for row in fullPhoto:  # count total '#'
    for col in row:
        if col == '#':
            total += 1
print(total - covered)
