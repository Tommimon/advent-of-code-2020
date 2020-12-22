def game(player1, player2):
    history = []
    while len(player1) != 0 and len(player2) != 0:
        state = {'player1': player1.copy(), 'player2': player2.copy()}
        if state in history:
            return True, player1 + player2
        history.append(state)
        num1 = player1.pop(0)
        num2 = player2.pop(0)
        if num1 <= len(player1) and num2 <= len(player2):
            winner, deck = game(player1[0:num1], player2[0:num2])
        else:
            winner = num1 > num2
        if winner:
            player1 += [num1, num2]
        else:
            player2 += [num2, num1]
    return len(player1) != 0, player1 + player2


paragraph = open("input.txt", "r").read().split('\n\n')
g1 = list(map(int, paragraph[0].split('\n')[1:]))
g2 = list(map(int, paragraph[1].split('\n')[1:]))
final = game(g1, g2)[1][::-1]  # get second result because is winner final deck
total = 0
for i in range(len(final)):
    total += (i + 1) * final[i]
print(total)
