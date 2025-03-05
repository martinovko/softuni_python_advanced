def bunny_spreader(matrix):
    bunnies_cor = []
    lost = False
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'B':
                bunnies_cor.append([row, col])
    for b in range(len(bunnies_cor)):
        r, c = bunnies_cor[b]
        if valid_index(r, (c - 1), matrix):
            if matrix[r][c - 1] == 'P':
                lost = True
            matrix[r][c - 1] = 'B'
        if valid_index(r, (c + 1), matrix):
            if matrix[r][c + 1] == 'P':
                lost = True
            matrix[r][c + 1] ='B'
        if valid_index(r - 1, c, matrix):
            if matrix[r - 1][c] == 'P':
                lost = True
            matrix[r - 1][c] = 'B'
        if valid_index((r + 1), c, matrix):
            if matrix[r + 1][c] == 'P':
                lost = True
            matrix[r + 1][c] = 'B'
    return lost, matrix

def valid_index(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[0])

n, m = [int(x) for x in input().split()]
lair = [[x for x in input()] for _ in range(n)]
commands = [x for x in input()]
player_r, player_c = 0, 0
win = False
game_lost = False

for r in range(len(lair)):
    for c in range(len(lair[r])):
        if lair[r][c] == 'P':
            player_r, player_c = r, c


for i in range(len(commands)):
    lair[player_r][player_c] = '.'
    if commands[i] == 'L':
        if valid_index(player_r,(player_c - 1), lair):
            player_c -= 1
            if lair[player_r][player_c] == 'B':
                game_lost, lair = bunny_spreader(lair)
                break
            else:
                lair[player_r][player_c] = 'P'
        else:
            win = True
        game_lost, lair = bunny_spreader(lair)
    elif commands[i] == 'R':
        if valid_index(player_r, (player_c + 1), lair):
            player_c += 1
            if lair[player_r][player_c] == 'B':
                game_lost, lair = bunny_spreader(lair)
                break
            else:
                lair[player_r][player_c] = 'P'
        else:
            win = True
        game_lost, lair = bunny_spreader(lair)
    elif commands[i] == 'U':
        if valid_index((player_r - 1), player_c, lair):
            player_r -= 1
            if lair[player_r][player_c] == 'B':
                game_lost, lair = bunny_spreader(lair)
                break
            else:
                lair[player_r][player_c] = 'P'
        else:
            win = True
        game_lost, lair = bunny_spreader(lair)
    elif commands[i] == 'D':
        if valid_index((player_r + 1), player_c, lair):
            player_r += 1
            if lair[player_r][player_c] == 'B':
                game_lost, lair = bunny_spreader(lair)
                break
            else:
                lair[player_r][player_c] = 'P'
        else:
            win = True
        game_lost, lair = bunny_spreader(lair)
    if win or game_lost:
        break

[print(*rows, sep='') for rows in lair]
if win:
    print(f'won: {player_r} {player_c}')
else:
    print(f'dead: {player_r} {player_c}')

