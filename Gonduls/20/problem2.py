lenght_line = 10
class Tile:
    def __init__(self, number, matrix):
        self.id = int(number)
        self.matrix = matrix
        # I need a unique representation of each side of a tile,
        # so i transform the string in a binary string and cast it to int.
        # normal is clockwise, mirrored is counter-clockwise
        self.up = conversion_to_num(matrix[0])
        self.down = conversion_to_num(matrix[-1][::-1])

        # Using list comprehension to get first (and then last) value of each line
        left = ''.join([matrix[-line][0] for line in range(1, lenght_line+1)])
        right = ''.join([matrix[line][-1] for line in range(lenght_line)])
        self.left = conversion_to_num(left)
        self.right = conversion_to_num(right)

        # For the mirrored values I just need to invert the viewing order of a mirrored matrix;
        # since mirrored matrixed are just flipped (I just switch the order I view the lines), 
        # I take those values for the mirrored matrix
        self.up_mir = conversion_to_num(matrix[0][::-1])
        self.down_mir = conversion_to_num(matrix[-1])
        self.left_mir = conversion_to_num(left[::-1])
        self.right_mir = conversion_to_num(right[::-1])
        self.sides = [self.up, self.right, self.down, self.left, self.up_mir, self.right_mir, self.down_mir, self.left_mir]
        
        # I have to keep track wether a tile has been mirrored yet or not
        self.mirrored = False
    

    # only prints sides and id
    def print_tile(self):
        print('Tile ', self.id)
        print(conversion_to_string(self.up))
        to_print_left = (conversion_to_string(self.left_mir))
        to_print_right = (conversion_to_string(self.right))
        for i in range(1, lenght_line - 1):
            print(to_print_left[i], ' '*(lenght_line-4), to_print_right[i])
        print(conversion_to_string(self.down_mir))
        print()


    # only prints the matrix
    def print_tile_matrix(self):
        for i in range(lenght_line):
            print(self.matrix[i])
        print("\n")
    

    # I only need one type of rotation, I'm choosing clockwise
    def rotate(self, times):
        for i in range(times % 4):
            # line used to obtain rotation of every element, obtained by trial and error (can't explain why it works but it does)
            self.matrix = [[self.matrix[line][column] for line in range(lenght_line-1,-1,-1)] for column in range(lenght_line)]
            self.matrix = ["".join(self.matrix[line]) for line in range(lenght_line)]
            self.up, self.right, self.down, self.left =  self.left, self.up, self.right, self.down
            self.up_mir, self.left_mir, self.down_mir, self.right_mir =  self.right_mir, self.up_mir, self.left_mir, self.down_mir

    
    # I only need to mirror it around the x axis (I just switch the lines so that the first line is the last and viceversa)
    def mirror(self):
        self.matrix = [self.matrix[line] for line in range(lenght_line-1, -1, -1)]
        self.mirrored = True

#conversion from binary (#,.) to int of sides, occupies less space
def conversion_to_num(string):
    return (int(string.replace('#','1').replace('.','0'),2))

#only used in print_tile to reconvert momentarily a side
def conversion_to_string(num):
    result = str(bin(num))[2:].replace('1','#').replace('0','.')
    return('.'*(lenght_line - len(result)) + result)


with open('./Gonduls/20/input.txt', 'r') as inputf:
    lista = inputf.read().split('\n')

count = 0
for line in lista:
    if 'Tile ' in line:
        count += 1

i = 0
tile_list = []
while i < count*(lenght_line + 2):
    number = int(lista[i][5:-1])
    matrix = []
    for j in range(1, 1 + len(lista[1])):
        matrix.append(lista[i + j])
    tile_list.append(Tile(number, matrix))
    i += 2 + len(lista[1])

#all_sides contains all sides (mirrored and not) of all tiles
all_sides = []
for el in tile_list:
    for side in el.sides:
        all_sides.append(side)

answer = 1
corners  = []
for el in tile_list:
    corner_sides = []
    unmatched = 0
    
    # I'm choosing to give (up, right, down, left) the indices (0, 1, 2, 3)
    for side in el.sides[:4]:
        if all_sides.count(side) == 1:
            unmatched += 1
            corner_sides.append(el.sides.index(side))
    if unmatched == 2:
        answer *= el.id
        corners.append([tile_list.index(el), corner_sides])

#print(answer)
############### start part 2 ####################

tiles_matrix = []
# corner is the tile's index in tile_list
for corner in corners:
    # I need to start from the top left corner, so I need a corner 
    # with unmatched sides up and left - [0, 3], following the indices
    if corner[1] == [0, 3]:
        tiles_matrix.append([corner[0]])
        break

# if none of the corner pieces I have found are turned the way I want them to be turned:
# I take the first corner (corners[0]) and turn it the way I want it.
# Since it can have only three orientations (if it made it to here it can only be ([0, 1], [1, 2] or [2, 3]))
# it will only need (3 - (0, 1, 2)) rotations to be in the right orientation, 
if len(tiles_matrix) != 1:
    tile_list[corners[0]].rotate(3 - corners[0][1][0])
    tiles_matrix.append([corners[0][0]])

#print(corners)
# I have to build the actual matrix
for line in range(lenght_line):
    for column in range(1, lenght_line):
        # previous_tile is the tile's index in tile_list
        previous_tile = tiles_matrix[line][column - 1]
        right = tile_list[previous_tile].right
        # tile is an actual tile, not an index
        for index, tile in enumerate(tile_list):
            if(index != previous_tile) and right in tile.sides:
                if right in tile.sides[:4]:
                    tile.mirror()
                while(right != tile.left_mir):
                    tile.rotate(1)
                tiles_matrix[line].append(index)
    if line != lenght_line - 1:
        down = tile_list[matrix[-1][0]].down
        for index, tile in enumerate(tile_list):
            if(index != matrix[-1][0]) and down in tile.sides:
                if down in tile.sides[4:]:
                    tile.mirror()
                while(down != tile.down):
                    tile.rotate(1)
                tile.mirror()
                tiles_matrix.append([])
                tiles_matrix[-1].append(index)
                break
        
        