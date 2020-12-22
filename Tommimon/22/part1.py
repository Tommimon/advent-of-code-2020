paragraph = open("input.txt", "r").read().split('\n\n')
player1 = list(map(int, paragraph[0].split('\n')[1:]))
player2 = list(map(int, paragraph[1].split('\n')[1:]))

while len(player1) != 0 and len(player2) != 0:
    num1 = player1.pop(0)
    num2 = player2.pop(0)
    if num1 > num2:
        player1 += [num1, num2]
    else:
        player2 += [num2, num1]

winner = (player1 + player2)[::-1]
total = 0
for i in range(len(winner)):
    total += (i + 1) * winner[i]
print(total)
