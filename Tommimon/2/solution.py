

def get_entry_parts(row):
    parts = row.split(' ')
    policy = parts[0].split('-')
    num1 = int(policy[0])
    num2 = int(policy[1])
    letter = parts[1][0]  # also remove ':'
    password = parts[2]
    return num1, num2, letter, password


def valid_pass_count(row):
    min_times, max_times, letter, password = get_entry_parts(row)
    occurrences = password.count(letter)
    if min_times <= occurrences <= max_times:
        return True
    return False


def valid_pass_pos(row):
    first_index, second_index, letter, password = get_entry_parts(row)
    correct_pos = 0
    if password[first_index-1] == letter:
        correct_pos += 1
    if password[second_index-1] == letter:
        correct_pos += 1
    if correct_pos == 1:
        return True
    return False


counter1 = 0
counter2 = 0

with open('input.txt', 'r') as file:
    for fullLine in file.readlines():
        line = fullLine[:-1]  # remove ending \n
        if valid_pass_count(line):
            counter1 += 1
        if valid_pass_pos(line):
            counter2 += 1

print(counter1)
print(counter2)
