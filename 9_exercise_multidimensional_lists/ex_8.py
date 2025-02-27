def valid_index(index1, index2, matrix):
    return 0 <= index1 < len(matrix) and 0 <= index2 < len(matrix[0])


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = [[x] for x in input().split()]
live_cells = 0
sum_live_cells = 0

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(len(coordinates)):
    cor_r1, cor_c1 = [int(x) for x in coordinates[i][0].split(',')]

    if matrix[cor_r1][cor_c1] > 0:
        for dr, dc in directions:
            new_r, new_c = cor_r1 + dr, cor_c1 + dc
            if valid_index(new_r, new_c, matrix) and matrix[new_r][new_c] > 0:
                matrix[new_r][new_c] -= matrix[cor_r1][cor_c1]

        matrix[cor_r1][cor_c1] = 0

# Count live cells and sum
for rows in matrix:
    for item in rows:
        if item > 0:
            live_cells += 1
            sum_live_cells += item

print(f'Alive cells: {live_cells}')
print(f'Sum: {sum_live_cells}')
[print(*row) for row in matrix]

# def valid_index(index1, index2, matrix):
#     if 0 <= index1 < len(matrix[0]) and 0 <= index2 < len(matrix):
#         return True
#
#
# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# coordinates = [[x] for x in input().split()]
# live_cells = 0
# sum_live_cells = 0
# for i in range(len(coordinates)):
#     cor_r1, cor_c1 = [int(x) for x in coordinates[i][0].split(',')]
#     if matrix[cor_r1][cor_c1] > 0:
#         if valid_index((cor_r1 - 1), (cor_c1 - 1), matrix) and matrix[cor_r1 - 1][cor_c1 - 1] > 0:
#             matrix[cor_r1 - 1][cor_c1 - 1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1 - 1), (cor_c1), matrix) and matrix[cor_r1 - 1][cor_c1] > 0:
#             matrix[cor_r1 - 1][cor_c1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1 - 1), (cor_c1 + 1), matrix)and matrix[cor_r1 - 1][cor_c1 + 1] > 0:
#             matrix[cor_r1 - 1][cor_c1 + 1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1), (cor_c1 -1), matrix) and matrix[cor_r1][cor_c1 - 1] > 0:
#             matrix[cor_r1][cor_c1 - 1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1), (cor_c1 + 1), matrix) and matrix[cor_r1][cor_c1 + 1] > 0:
#             matrix[cor_r1][cor_c1 + 1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1 + 1), (cor_c1 - 1), matrix) and matrix[cor_r1 + 1][cor_c1 - 1] > 0:
#             matrix[cor_r1 + 1][cor_c1 - 1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1 + 1), (cor_c1), matrix) and matrix[cor_r1 + 1][cor_c1] > 0:
#             matrix[cor_r1 + 1][cor_c1] -= matrix[cor_r1][cor_c1]
#         if valid_index((cor_r1 + 1), (cor_c1 + 1), matrix) and matrix[cor_r1 + 1][cor_c1 + 1] > 0:
#             matrix[cor_r1 + 1][cor_c1 + 1] -= matrix[cor_r1][cor_c1]
#         matrix[cor_r1][cor_c1] = 0
#
# for rows in matrix:
#     for item in rows:
#         if item > 0:
#             live_cells += 1
#             sum_live_cells += item
#
# print(f'Alive cells: {live_cells}')
# print(f'Sum: {sum_live_cells}')
# [print(*row) for row in matrix]
