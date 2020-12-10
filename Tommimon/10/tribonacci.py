def tribonacci(n):
    a = 1.839286755
    b = -0.4196433776-0.6062907292j
    c = -0.4196433776+0.6062907292j
    return round((a**n/(-a**2+4*a-1) + b**n/(-b**2+4*b-1) + c**n/(-c**2+4*c-1)).real)


with open('input.txt', 'r') as file:
    numbers = [0] + sorted(list(map(int, file.read().split('\n'))))
consecutive = 1
ris = 1
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i-1] == 1:
        consecutive += 1
    else:
        ris *= tribonacci(consecutive)
        consecutive = 1
print(ris * tribonacci(consecutive))
