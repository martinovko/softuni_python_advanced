n = int(input())
field = []
bunny = [0, 0]
ways = {'up':(-1, 0), 'down':(1, 0), 'left':(0, -1), 'right':(0, 1)}
max_way = ''
current_egg_positions = []
current_egg_sum = 0
max_eggs = -float('inf')
max_positions = []

for row in range(n):
    field.append(input().split())
    for col in range(n):
        if field[row][col] == 'B':
            bunny = [row, col]

for way in ways.items():
    current_egg_sum = 0
    current_egg_positions = []
    r = bunny[0] + way[1][0]
    c = bunny[1] + way[1][1]
    while 0 <= r < n and 0 <= c < n:
        if field[r][c] != 'X':
            current_egg_sum += int(field[r][c])
            current_egg_positions.append([r, c])
        else:
             break
        r += way[1][0]
        c += way[1][1]
    if current_egg_sum > max_eggs and current_egg_positions:
        max_eggs = current_egg_sum
        max_way = way[0]
        max_positions = current_egg_positions
print(max_way)
if max_positions:
    print(*max_positions, sep='\n')
print(max_eggs)




