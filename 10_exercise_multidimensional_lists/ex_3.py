def is_valid(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[0])

n = int(input())

board = []
knights = []
greatest_knights = []
greatest_hits = 0
current_knight_hits = 0
coordinates = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
removed_knights = 0

for row in range(n):
    board.append([x for x in input()])
    for col in range(n):
        if board[row][col] == 'K':
            knights.append([row, col])

while True:
    greatest_hits = 0
    greatest_knights = []
    for k, c in knights:
        current_knight_hits = 0
        for cor1, cor2  in coordinates:
            new_k = k + cor1
            new_c = c + cor2
            if is_valid(new_k, new_c, board):
                if board[new_k][new_c] == 'K':
                    current_knight_hits += 1
        if current_knight_hits > greatest_hits:
            greatest_knights = [k, c]
            greatest_hits = current_knight_hits
    if greatest_hits < 1:
        break
    knights.remove(greatest_knights)
    board[greatest_knights[0]][greatest_knights[1]] = '0'
    removed_knights += 1
print(removed_knights)



