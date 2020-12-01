
with open('input.txt', 'r') as file:
    for line in file.readlines():
        row = line[:-1]  # remove ending \n
        print(row)
