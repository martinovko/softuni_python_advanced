rows, cols = [int(x) for x in input().split()]

square_matrices = 0

matrix = [[x for x in input().split()] for _ in range(rows)]

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            square_matrices += 1

print(square_matrices)