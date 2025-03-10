def cookie(santa_r, santa_c, n, neighbourhood, m, sad_nice_kids):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in direction:
        new_r, new_c = santa_r + dr, santa_c + dc
        if 0 <= new_r < n and 0 <= new_c < n and neighbourhood[new_r][new_c] != '-':
            m -= 1
            if neighbourhood[new_r][new_c] == 'V':
                sad_nice_kids -= 1
            neighbourhood[new_r][new_c] = '-'

    return m, sad_nice_kids, neighbourhood

def presents(santa_r, santa_c, santa, m, sad_nice_kids, neighbourhood):
    if neighbourhood[santa_r][santa_c] == 'V':
        neighbourhood[santa_r][santa_c] = 'S'
        m -= 1
        sad_nice_kids -= 1
        santa = [santa_r, santa_c]
    elif neighbourhood[santa_r][santa_c] == 'X':
        neighbourhood[santa_r][santa_c] = 'S'
        santa = [santa_r, santa_c]
    elif neighbourhood[santa_r][santa_c] == 'C':
        neighbourhood[santa_r][santa_c] = 'S'
        santa = [santa_r, santa_c]
        m, sad_nice_kids, neighbourhood = cookie(santa_r, santa_c, n, neighbourhood, m, sad_nice_kids)
    else:
        neighbourhood[santa_r][santa_c] = 'S'
        santa = [santa_r, santa_c]
    return santa, m, sad_nice_kids, neighbourhood



m = int(input()) # presents
n = int(input()) # neighbourhood
neighbourhood = []
nice_kids = 0
sad_nice_kids = 0
santa = [0, 0]
cookies = []

for row in range(n):
    neighbourhood.append(input().split())
    for col in range(n):
        if neighbourhood[row][col] == 'S':
            santa = [row, col]
        if neighbourhood[row][col] == 'V':
            nice_kids += 1
            sad_nice_kids += 1

command = input()
while True and command != 'Christmas morning':
    santa_r = santa[0]
    santa_c = santa[1]
    if command == 'up' and 0 <= santa_r - 1 < n:
        neighbourhood[santa_r][santa_c] = '-'
        santa_r -= 1
        santa, m, sad_nice_kids, neighbourhood = presents(santa_r, santa_c, santa, m, sad_nice_kids, neighbourhood)
    if command == 'down' and 0 <= santa_r + 1 < n:
        neighbourhood[santa_r][santa_c] = '-'
        santa_r += 1
        santa, m, sad_nice_kids, neighbourhood = presents(santa_r, santa_c, santa, m, sad_nice_kids, neighbourhood)
    if command == 'left' and 0 <= santa_c - 1 < n:
        neighbourhood[santa_r][santa_c] = '-'
        santa_c -= 1
        santa, m, sad_nice_kids, neighbourhood = presents(santa_r, santa_c, santa, m, sad_nice_kids, neighbourhood)
    if command == 'right' and 0 <= santa_c + 1 < n:
        neighbourhood[santa_r][santa_c] = '-'
        santa_c += 1
        santa, m, sad_nice_kids, neighbourhood = presents(santa_r, santa_c, santa, m, sad_nice_kids, neighbourhood)
    if m < 1:
        break
    command = input()

if m < 1 and sad_nice_kids > 0:
    print('Santa ran out of presents!')
[print(*row) for row in neighbourhood]
if sad_nice_kids < 1:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {sad_nice_kids} nice kid/s.")

