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

        
        # I have to keep track wether a tile has been mirrored yet or not
        self.mirrored = False
    
    def print_tile(self):
        print('Tile ', self.id)
        print(conversion_to_string(self.up))
        to_print_left = (conversion_to_string(self.left_mir))
        to_print_right = (conversion_to_string(self.right))
        for i in range(1, lenght_line - 1):
            print(to_print_left[i], ' '*(lenght_line-4), to_print_right[i])
        print(conversion_to_string(self.down_mir))
        print()

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

#sides contains all sides (mirrored and not) of all tiles
sides = []
for el in tile_list:
    curr_sides = [el.up, el.down, el.left, el.right, el.up_mir, el.down_mir, el.left_mir, el.right_mir] #
    for side in curr_sides:
        sides.append(side)

answer = 1
corners  = []

for el in tile_list:
    corner_sides = []
    unmatched = 0
    curr_sides = [el.up, el.right, el.down, el.left]
    curr_mirrored = [el.up_mir, el.right_mir, el.down_mir, el.left_mir]
    for side in curr_sides:
        if sides.count(side) - curr_mirrored.count(side) - curr_sides.count(side) == 0:
            unmatched += 1
            corner_sides.append(curr_sides.index(side))
    if unmatched == 2:
        answer *= el.id
        corners.append([tile_list.index(el), corner_sides])

print(corners)
#print(answer)

#tile_list[1].print_tile_matrix()
#tile_list[1].mirror()
#tile_list[1].print_tile_matrix()
#tile_list[1].rotate(3)
#tile_list[1].print_tile_matrix()