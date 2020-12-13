# implementing diofante equation algoritm from https://it.wikipedia.org/wiki/Equazione_diofantea_lineare
# to solve divisions with modulus operator
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def time(ratio1, ratio2, shift):
    target = ratio2 - (shift % ratio2)  # class target
    moltiplicator = division(target, ratio1 % ratio2, ratio2)
    return moltiplicator * ratio1 + shift


def division(dividend, divisor, modulus):
    res = resolution(modulus, divisor)[1]  # solve equation: n*modolus + res*divisor = 1
    res = res * dividend % modulus
    return res


def resolution(r1, r2):
    q = r1 // r2
    r3 = r1 % r2
    if r3 == 1:
        return 1, -q
    low, high = resolution(r2, r3)
    return high, low + high * (-q)


with open('input.txt', 'r') as file:
    file.readline()
    ids = file.readline().split(',')
totalRatio = int(ids[0])
totalShift = 0
for i, n in enumerate(ids):
    if n != 'x' and i != 0:
        totalShift = time(totalRatio, int(n), totalShift + i) - i
        totalRatio = lcm(totalRatio, int(n))
print(totalShift)
