from reverseprint import reverse_print

summation = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        row = line[:-1]  # remove ending \n
        summation += int(line)

print(summation)
reverse_print(summation)
