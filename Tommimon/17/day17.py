class Dimension:
    def __init__(self, dim, size=None, val=None):
        self.dim = dim
        if size is None:
            self.size = [1] * dim
        else:
            self.size = size
        if dim == 0:
            if val is None:
                self.children = '.'
            else:
                self.children = val
        else:
            self.children = []
            for i in range(self.size[dim-1]):
                self.children.append(Dimension(dim - 1, self.size))

    def turn(self):
        Dimension.for_elem(self.size, self.check_all)
        self.write_all()
        self.expand_size()

    @staticmethod
    def for_elem(size, callback, pos=None):
        if pos is None:
            pos = []
        if len(size) == 0:
            callback(pos)
        else:
            for i in range(size[0]):
                Dimension.for_elem(size[1:], callback, pos + [i])

    def check_all(self, pos):
        near = self.count_near(pos)
        elem = self.get_elem(pos)
        if elem == '#':
            if near != 2 and near != 3:
                self.set_elem(pos, '0')
        elif elem == '.':
            if near == 3:
                self.set_elem(pos, '1')

    def count_near(self, pos, diff=False):
        if self.dim == 0:
            if diff and (self.children == '#' or self.children == '0'):
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

    def write_all(self):
        if self.dim == 0:
            if self.children == '0':
                self.children = '.'
            elif self.children == '1':
                self.children = '#'
        else:
            for elem in self.children:
                elem.write_all()

    def expand_size(self):
        for i in range(len(self.size)):
            self.size[i] += 2
        self.expand_all()

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

    def count_total(self):
        if self.dim == 0:
            if self.children == '#':
                return 1
            return 0
        total = 0
        for elem in self.children:
            total += elem.count_total()
        return total

    def print(self):
        for elem in self.children:
            print(elem.to_list())

    def to_list(self):
        if self.dim == 0:
            return self.children
        return list(map(lambda e: e.to_list(), self.children))


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
length = len(lines[0]) + 2
space3D = Dimension(3, [length] * 3)
for index, line in enumerate(lines):
    row = list(map(lambda e: Dimension(0, space3D.size, e), ['.'] + list(line) + ['.']))
    space3D.children[length // 2].children[index + 1].children = row
for index in range(6):
    space3D.turn()
print(space3D.count_total())
space4D = Dimension(4, [length] * 4)
for index, line in enumerate(lines):
    row = list(map(lambda e: Dimension(0, space4D.size, e), ['.'] + list(line) + ['.']))
    space4D.children[length // 2].children[length // 2].children[index + 1].children = row
for index in range(6):
    space4D.turn()
print(space4D.count_total())
