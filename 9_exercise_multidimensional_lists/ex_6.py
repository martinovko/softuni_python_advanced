def valid_swap(s_1, s_2, s_3, s_4, mat):
    if 0 <= s_1 <= len(mat[0]) and 0 <= s_2 <= len(mat) and 0 <= s_3 <= len(mat[0]) and 0 <= s_4 <= len(mat):
        return True

rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

command = input().split()

while command[0] != 'END':
    if len(command) == 5 and command[0] == 'swap' and valid_swap(int(command[1]), int(command[2]), int(command[3]), int(command[4]), matrix):
            matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
            [print(*row) for row in matrix]
    else:
        print('Invalid input!')
    command = input().split()