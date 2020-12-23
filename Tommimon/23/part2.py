class Cup:
    def __init__(self, val, suc):
        self.val = val
        self.suc = suc


class CupList:
    def __init__(self, val_list):
        self.len = len(val_list)
        # in the catalog at index n there is the cup with label n
        self.catalog = [Cup(0, None)] * (self.len + 1)  # using cup placeholders
        if len(val_list) == 0:
            self.first = None
        else:
            self.first = Cup(val_list[0], None)
            self.catalog[self.first.val] = self.first
            prec = self.first
            last = self.first
            for v in val_list[1:]:
                last = Cup(v, None)
                self.catalog[last.val] = last
                prec.suc = last
                prec = prec.suc
            last.suc = self.first  # close circular list


def is_picked(first_picked, val):
    p = first_picked
    for i in range(3):
        if p.val == val:
            return True
        p = p.suc
    return False


def move(cups, turns):
    size = cups.len
    curr = cups.first
    for i in range(turns):
        p = curr.suc
        first_picked = p
        last_picked = None
        for j in range(3):
            last_picked = p
            p = p.suc  # at the end p is the element to concat to curr (the next curr)
        curr.suc = p  # this remove picked from list
        dest_num = (curr.val - 2) % size + 1
        while is_picked(first_picked, dest_num):  # find destination number
            dest_num = (dest_num - 2) % size + 1
        dest = cups.catalog[dest_num]  # get destination cup from catalog
        closing = dest.suc
        dest.suc = first_picked
        last_picked.suc = closing
        curr = curr.suc  # change current


puzzleInput = '487912365'

totalCups = 1000000
moves = 10000000
labelList = list(map(int, puzzleInput)) + list(range(len(puzzleInput) + 1, totalCups + 1))
cupList = CupList(labelList)
move(cupList, moves)
c = cupList.first
while c.val != 1:
    c = c.suc
print(c.suc.val * c.suc.suc.val)
