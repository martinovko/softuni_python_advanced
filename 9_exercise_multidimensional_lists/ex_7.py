from collections import deque

n, m = [int(x) for x in input().split()]

string = [x for x in input()]
matrix = []
adding = deque()
for row in range(n):
    adding = deque()
    if row % 2 != 0:
        for col in range(1, m + 1):
            adding.appendleft(string[0])
            string.append(string.pop(0))
    else:
        for col in range(m):
            adding.append(string[0])
            string.append(string.pop(0))
    matrix.append(adding)
[print(*row, sep='') for row in matrix]