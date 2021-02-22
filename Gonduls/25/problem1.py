with open('Gonduls/25/input.txt') as file:
    public_keys = tuple(map(int, file.read().split('\n')))

subject_number = 7
loop_size = 0
value = 1
while(value != public_keys[0]):
    value *= subject_number
    value = value % 20201227
    loop_size += 1

value = 1
subject_number = public_keys[1]
while(loop_size):
    loop_size -= 1
    value *= subject_number
    value = value % 20201227

print(value)