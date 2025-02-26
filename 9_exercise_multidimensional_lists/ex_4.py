rows, cols = [int(x) for x in input().split()]

main_matrix = [[int(x) for x in input().split()] for _ in range(rows)]
sub_matrix = []
max_matrix = []
max_sum = -float('inf')

for i in range(rows - 2):
    for j in range(cols - 2):
        sub_matrix = []
        sub = []
        for r in range(i, i + 3):
            sub = []
            for c in range(j, j + 3):
                sub.append(main_matrix[r][c])
            sub_matrix.append(sub)
        if sum(sum(rows) for rows in sub_matrix) > max_sum and len(sub_matrix) > 1:
            max_sum = sum(sum(rows) for rows in sub_matrix)
            max_matrix = sub_matrix
print(f'Sum = {max_sum}')
[print(*row) for row in max_matrix]