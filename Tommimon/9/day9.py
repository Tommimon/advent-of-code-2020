offset = 25
invalid = 0
with open('input.txt', 'r') as file:
    numbers = list(map(int, file.read().split('\n')))
for i, num in enumerate(numbers[offset:]):
    found = False
    for j in numbers[i:i+offset]:
        for k in numbers[i:i+offset]:
            if j != k:
                if num == j+k:
                    found = True
    if not found:
        invalid = num
        break
print(invalid)
summation = 0
start = 0
end = 0
while True:
    if summation < invalid:
        summation += numbers[end]
        end += 1
    if summation == invalid:
        break
    elif summation > invalid:
        summation -= numbers[start]
        start += 1
print(max(numbers[start:end]) + min(numbers[start:end]))
