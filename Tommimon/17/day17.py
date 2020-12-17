# represent a n-dimensional block: element, row, slice ...
class Dimension:
    # all the children of a dimension are other dimensions that shares the same size list (not a copy)
    # if I change the size list it changes for all the children and parents
    # the element of size with index n is relative to the n+1 dimensions (size[0] decide rows length)
    def __init__(self, dim, size=None, val=None):
        self.dim = dim
        if size is None:
            self.size = [1] * dim  # is bigger dimension so create the shared size list
        else:
            self.size = size
        if dim == 0:
            if val is None:  # the 0-dimension block has no list as children but a single character
                self.children = '.'  # default value
            else:
                self.children = val
        else:
            self.children = []
            for i in range(self.size[dim-1]):
                self.children.append(Dimension(dim - 1, self.size))

    def cycle(self):
        Dimension.for_each_elem(self.size, self.check_elem)
        self.do_changes()
        for i in range(len(self.size)):  # add new margin
            self.size[i] += 2
        self.expand_all()

    # run callback once for each single element and pass coordinates vector as parameter
    @staticmethod
    def for_each_elem(size, callback, pos=None):
        if pos is None:
            pos = []
        if len(size) == 0:
            callback(pos)
        else:
            for i in range(size[0]):
                Dimension.for_each_elem(size[1:], callback, [i] + pos)

    # if the element with coordinates pos must change set it to '0' or '1'
    # '0' is a '#' going to be '.' (but is still a '#')
    # '1' is a '.' going to be '#' (but is still a '.')
    def check_elem(self, pos):
        near = self.count_near(pos)
        elem = self.get_elem(pos)
        if elem == '#':
            if near != 2 and near != 3:
                self.set_elem(pos, '0')
        elif elem == '.':
            if near == 3:
                self.set_elem(pos, '1')

    # count neighbour '#'
    def count_near(self, pos, diff=False):
        if self.dim == 0:
            if diff and (self.children == '#' or self.children == '0'):  # '0' is still '#'
                return 1
            return 0
        counter = 0
        if pos[0] > 0:
            counter += self.children[pos[0] - 1].count_near(pos[1:], True)
        if pos[0] < len(self.children) - 1:
            counter += self.children[pos[0] + 1].count_near(pos[1:], True)
        counter += self.children[pos[0]].count_near(pos[1:], diff)
        return counter

    def get_elem(self, pos):
        if self.dim == 0:
            return self.children
        return self.children[pos[0]].get_elem(pos[1:])

    def set_elem(self, pos, val):
        if self.dim == 0:
            self.children = val
        else:
            self.children[pos[0]].set_elem(pos[1:], val)

    # change the '0' and '1' to what they must became ('.' and '#')
    def do_changes(self):
        if self.dim == 0:
            if self.children == '0':
                self.children = '.'
            elif self.children == '1':
                self.children = '#'
        else:
            for elem in self.children:
                assert isinstance(elem, Dimension)
                elem.do_changes()

    def expand_all(self):
        if self.dim > 1:
            for elem in self.children:
                elem.expand_all()
        self.append()
        self.prepend()

    def append(self):
        self.children.append(Dimension(self.dim - 1, self.size))

    def prepend(self):
        self.children.insert(0, Dimension(self.dim - 1, self.size))

    # count '#'
    def count_total(self):
        if self.dim == 0:
            if self.children == '#':
                return 1
            return 0
        total = 0
        for elem in self.children:
            total += elem.count_total()
        return total

    # print dimension for debug
    # first dimension is splitted on different lines, the others are all on one line
    def print(self):
        for elem in self.children:
            print(elem.to_list())

    # convert dimension to lists inside lists...
    def to_list(self):
        if self.dim == 0:
            return self.children
        return list(map(lambda e: e.to_list(), self.children))


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
length = len(lines[0]) + 2  # add margin to create new '#' on the border
space3D = Dimension(3, [length, length, 3])  # define dimension and sizes
for index, line in enumerate(lines):  # insert input in dimension
    row = list(map(lambda e: Dimension(0, space3D.size, e), ['.'] + list(line) + ['.']))
    space3D.children[1].children[index + 1].children = row
for index in range(6):
    space3D.cycle()
print(space3D.count_total())
space4D = Dimension(4, [length, length, 3, 3])
for index, line in enumerate(lines):
    row = list(map(lambda e: Dimension(0, space4D.size, e), ['.'] + list(line) + ['.']))
    space4D.children[1].children[1].children[index + 1].children = row
for index in range(6):
    space4D.cycle()
print(space4D.count_total())
