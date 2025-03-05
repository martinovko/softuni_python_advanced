def player (matrix): #finds 's' in the matrix to know where to start
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 's':
                return r, c #return coordinates
    return None

def coal_counter(matrix):
    coals = 0
    for r in matrix:
        for c in r:
            if c == 'c':
                coals += 1
    return coals

def valid_index(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[0])


n = int(input())
commands = input().split()
field = [[x for x in input().split()] for _ in range(n)]

miner_r, miner_c = player(field)
coal = coal_counter(field)
game_on = True
new_r, new_c = 0, 0

while commands:
    if commands[0] == 'left':
        commands.pop(0)
        if valid_index(miner_r, (miner_c - 1), field):
            new_r, new_c = miner_r, miner_c - 1
            if field[new_r][new_c] == "c":
                coal -= 1
                field[new_r][new_c] = '*'
            if field[new_r][new_c] =='e':
                game_on = False
        miner_r, miner_c = new_r, new_c


    elif commands[0] == 'right':
        commands.pop(0)
        if valid_index(miner_r, (miner_c + 1), field):
            new_r, new_c = miner_r, miner_c + 1
            if field[new_r][new_c] == "c":
                coal -= 1
                field[new_r][new_c] = '*'
            if field[new_r][new_c] =='e':
                game_on = False
        miner_r, miner_c = new_r, new_c

    elif commands[0] == 'up':
        commands.pop(0)
        if valid_index((miner_r - 1), miner_c, field):
            new_r, new_c = miner_r - 1, miner_c
            if field[new_r][new_c] == "c":
                coal -= 1
                field[new_r][new_c] = '*'
            if field[new_r][new_c] =='e':
                game_on = False
        miner_r, miner_c = new_r, new_c

    elif commands[0] == 'down':
        commands.pop(0)
        if valid_index((miner_r + 1), miner_c, field):
            new_r, new_c = miner_r + 1, miner_c
            if field[new_r][new_c] == "c":
                coal -= 1
                field[new_r][new_c] = '*'
            if field[new_r][new_c] =='e':
                game_on = False
        miner_r, miner_c = new_r, new_c

    if coal < 1:
        print(f'You collected all coal! ({miner_r}, {miner_c})')
        break
    if not game_on:
        print(f'Game over! ({miner_r}, {miner_c})')
if coal >= 1 and game_on:
    print(f'{coal} pieces of coal left. ({miner_r}, {miner_c})')
