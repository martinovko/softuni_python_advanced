rows, cols = [int(x) for x in input().split()]

matrix = []
adding = []
for row in range(rows):
    adding = []
    for col in range(cols):
        adding.append(f'{chr(97 + row)}{chr(97 + col + row)}{chr(97 + row)}')
    matrix.append(adding)
[print(*row) for row in matrix]