with open('input.txt', 'r') as file:
    numbers = [0] + list(map(int, file.read().split('\n')))
threes = ((max(numbers) + 3) - len(numbers)) // 2
print((len(numbers) - threes) * threes)
