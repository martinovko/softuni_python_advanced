n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while command[0] != 'END':
    if 0 <= int(command[1]) < n and 0 <= int(command[2]) < n:
        if command[0] == 'Add':
            matrix[int(command[1])][int(command[2])] += int(command[3])
        elif command[0] == 'Subtract':
            matrix[int(command[1])][int(command[2])] -= int(command[3])
    else: print('Invalid coordinates')
    command = input().split()

[print(*row) for row in matrix]