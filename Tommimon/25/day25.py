subject = 7
divider = 20201227


def calc_size(public):
    val = 1
    count = 0
    while val != public:
        val = (val * subject) % divider
        count += 1
    return count


def transform(size, subj=1):
    val = 1
    for _ in range(size):
        val = (val * subj) % divider
    return val


cardPublic, doorPublic = tuple(map(int, open('input.txt').read().split('\n')))
print(transform(calc_size(cardPublic), doorPublic))
