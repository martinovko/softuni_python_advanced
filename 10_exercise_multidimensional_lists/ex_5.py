n = int(input())
wonderland = []

a = [0, 0]
tea = 0

for row in range(n):
    wonderland.append(input().split())
    for col in range(n):
        if wonderland[row][col] == 'A':
            a = [row, col]
            wonderland[row][col] = '*'

while True and tea < 10:
    command = input()
    if command == 'up':
        if 0 <= a[0] - 1 < n:
            a[0] -= 1
            if wonderland[a[0]][a[1]] in '0123456789 10':
                tea += int(wonderland[a[0]][a[1]])
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == '*' or wonderland[a[0]][a[1]] == '.':
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == 'R':
                wonderland[a[0]][a[1]] = '*'
                break
        else:
            break
    elif command == 'down':
        if 0 <= a[0] + 1 < n:
            a[0] += 1
            if wonderland[a[0]][a[1]] in '0123456789 10':
                tea += int(wonderland[a[0]][a[1]])
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == '*' or wonderland[a[0]][a[1]] == '.':
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == 'R':
                wonderland[a[0]][a[1]] = '*'
                break
        else:
            break
    elif command == 'left':
        if 0 <= a[1] - 1 < n:
            a[1] -= 1
            if wonderland[a[0]][a[1]] in '0123456789 10':
                tea += int(wonderland[a[0]][a[1]])
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == '*' or wonderland[a[0]][a[1]] == '.':
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == 'R':
                wonderland[a[0]][a[1]] = '*'
                break
        else:
            break
    elif command == 'right':
        if 0 <= (a[1] + 1) < n:
            a[1] += 1
            if wonderland[a[0]][a[1]] in '0123456789 10':
                tea += int(wonderland[a[0]][a[1]])
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == '*' or wonderland[a[0]][a[1]] == '.':
                wonderland[a[0]][a[1]] = '*'
            elif wonderland[a[0]][a[1]] == 'R':
                wonderland[a[0]][a[1]] = '*'
                break
        else:
            break
if tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in wonderland]



