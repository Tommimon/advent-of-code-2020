import re


def num_between(val, n_min, n_max):
    if len(val) == len(str(n_max)):
        try:
            num = int(val)
            return n_min <= num <= n_max
        except TypeError:
            return False


def valid_pair(key, value):
    if key == 'byr':
        return num_between(value, 1920, 2002)
    elif key == 'iyr':
        return num_between(value, 2010, 2020)
    elif key == 'eyr':
        return num_between(value, 2020, 2030)
    elif key == 'hgt':
        if value[-2:] == 'cm':
            return num_between(value[:-2], 150, 193)
        if value[-2:] == 'in':
            return num_between(value[:-2], 59, 76)
    elif key == 'hcl':
        if value[0] == '#':
            for c in value[1:]:
                if c not in '0123456789abcdef':
                    return False
            return True
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return num_between(value, 0, 999999999)
    return False


with open('input.txt', 'r') as file:
    passports = file.read().split('\n\n')
    counter1 = 0
    counter2 = 0
    for pp in passports:
        pairs = re.split('\n| ', pp)
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        valid = True
        for p in pairs:
            key = p.split(':')[0]
            if key in required:
                required.remove(key)
                valid = valid and valid_pair(key, p.split(':')[1])
        if len(required) == 0:
            counter1 += 1
            if valid:
                counter2 += 1
print(counter1)
print(counter2)
