#
#                PROBLEM INTERPRETATION                |                       MY INTERPRETATION
#                                                      |
#                         West                         |                             West
#                        _______                       |                            _______
#        *South-West*   /       \   North-West         |                 *South*   /       \   North-West
#                      /         \                     |                          /         \
#                      \         /                     |                          \         /
#           South-Est   \_______/   *North-Est*        |               South-Est   \_______/   *North*
#                          Est                         |                              Est
#                                                      |
#                                                      |
#                                                      |
#               --------------------> Est              |
#                                                      |              --------------------> Est
#            /                         \               |      |                                     .
#           /      / \ / \ / \ / \      \              |      |      _____________________________    .
#          /      | A | B | C | D |      \             |      |     |  A  |  B  |  C  |  D  |     |     .
#         /      / \ / \ / \ / \ / \      \            |      |     |_____|_____|_____|_____|_____|       .
#        /      | E | F | G | H | I |      \           |      |     |  E  |  F  |  G  |  H  |  I  |         .
#       /        \ / \ / \ / \ / \ /        \          |      |     |_____|_____|_____|_____|_____|           .
#      /          | J | K | L | M |          \         |      |     |     |  J  |  K  |  L  |  M  |             .
#     |/           \ / \ / \ / \ /           \|        |     \|/    |_____|_____|_____|_____|_____|               .
#     '                                       '        |      '                                                    _|
# *South-West*                            South-Est    |   *South*                                             South-Est
#

def resize(list_, radius, default):  # resize generic list, expanding symmetrically
    for _ in range((size(radius) - len(list_)) // 2):
        list_.append(safe_copy(default))
        list_.insert(0, safe_copy(default))


def safe_copy(element):
    try:
        return element.copy()
    except AttributeError:
        return element


def size(radius):  # given the radius (max index abs value) the size is 2 radius + 1 for the center + 2 for margins
    return 2 * radius + 3


def resize_floor(f, s_radius, e_radius):
    resize(f, s_radius, ['.'] * size(e_radius))
    for r in floor:
        resize(r, e_radius, '.')


def is_margin(num, radius):
    return num == 0 or num == size(radius) - 1


# part 1
blacks = set()
for tile in open("input.txt", "r").read().split('\n'):
    tile = tile.replace('sw', 's').replace('ne', 'n')
    s = tile.count('s') - tile.count('n')
    e = tile.count('e') - tile.count('w')
    coords = (s, e)
    if coords in blacks:
        blacks.remove(coords)
    else:
        blacks.add(coords)
print(len(blacks))

# part 2
sRadius = 0  # radius is max coord in abs value
eRadius = 0
floor = [['.']]
for tile in blacks:  # set starting black tiles (from part 1 set) to '#'
    sRadius = max(sRadius, abs(tile[0]))
    eRadius = max(eRadius, abs(tile[1]))
    resize_floor(floor, sRadius, eRadius)
    floor[tile[0] + sRadius + 1][tile[1] + eRadius + 1] = '#'  # +1 for margin

for _ in range(100):
    expandS = 0
    expandE = 0
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            neighbours = 0
            for delta in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]:  # count neighbours
                y = i + delta[0]
                x = j + delta[1]
                if 0 <= y < len(floor) and 0 <= x < len(floor[i]):
                    if floor[y][x] == '#' or floor[y][x] == '0':
                        neighbours += 1
            if floor[i][j] == '#':  # decide changes but don't apply yet
                if neighbours == 0 or neighbours > 2:
                    floor[i][j] = '0'  # '0' is '#' going to '.'
            if floor[i][j] == '.':
                if neighbours == 2:
                    floor[i][j] = '1'  # '1' is '.' going to '#'
    for i in range(len(floor)):  # apply changes
        for j in range(len(floor[i])):
            if floor[i][j] == '0' or floor[i][j] == '1':
                if floor[i][j] == '0':
                    floor[i][j] = '.'
                else:
                    floor[i][j] = '#'
                if is_margin(i, sRadius):  # expand radius if I'm writing on margin
                    expandS = 1
                if is_margin(j, eRadius):
                    expandE = 1
    sRadius += expandS
    eRadius += expandE
    resize_floor(floor, sRadius, eRadius)

total = 0  # count final number of '#'
for row in floor:
    total += row.count('#')
print(total)
