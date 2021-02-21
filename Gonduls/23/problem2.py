class cup:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class cups_circle:
    def __init__(self):
        self.curr = None
    
    def append(self, value):
        if not self.curr:
            self.curr = cup(value)
            self.curr.next = self.curr
            self.curr.prev = self.curr
            return
        last = self.curr.prev
        last.next = cup(value)
        last.next.prev = last
        last = last.next
        last.next = self.curr
        self.curr.prev = last
        
    def find(self, value):
        punt = self.curr
        back_punt = self.curr
        while True:
            if punt.value == value:
                return(punt)
            if back_punt.value == value:
                return(back_punt)
            punt = punt.next
            back_punt = back_punt.prev
            if(punt == back_punt):
                print('Not found')
                return None
    
    def print_(self, amount):
        punt = self.curr
        for i in range(amount):
            print(punt.value)
            punt = punt.next
    
    # done so that it always takes out starting from current
    def take_out(self, amount = 3):
        start = self.curr.next
        punt = start
        for i in range(amount - 1):
            punt = punt.next
        self.curr.next = punt.next
        self.curr.next.prev = self.curr
        # returning a circle
        start.prev = punt
        punt.next = start
        return(start)

    def insert_circle(self, head, previous):
        tail = head.prev
        following = previous.next
        previous.next = head
        head.prev = previous
        tail.next = following
        following.prev = tail
        
    def list_cups(self):
        answer = []
        for i in range(1,10):
            answer.append(self.find(i))
        punt = self.find(10)
        for i in range(10, 1000001):
            answer.append(punt)
            punt = punt.next
        return answer

############################## Program start #####################
input = 215694783
max_l = 1000000
cups = list(map(lambda el: int(el), str(input))) #showoff
cups.extend(list(range(10, max_l +1)))
whole_circle = cups_circle()

for label in cups:
    whole_circle.append(label)

# cups_cup contains an indexed list of all cups, so that I don't have to search for them
cups_cup = whole_circle.list_cups()
for i in range (10000000):
    #print(i)
    three = whole_circle.take_out()
    dest = whole_circle.curr.value - 1
    while (dest in (three.value, three.next.value, three.prev.value)) and dest>0:
        dest -= 1
    if dest == 0:
        for el in cups_cup[::-1]:
            if el.value not in (three.value, three.next.value, three.prev.value):
                dest = el
                break
    else:
        dest = cups_cup[dest-1]
    whole_circle.insert_circle(three, dest)
    whole_circle.curr = whole_circle.curr.next
print(cups_cup[0].next.value * cups_cup[0].next.next.value)
#print(cups[cups.index(1) -max_l +1] * cups[cups.index(1) -max_l +2])