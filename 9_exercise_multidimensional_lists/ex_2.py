n = int(input())

matrix = [[int(x) for x in input().split()] for num in range(n)]

primary_diagonal = 0
secondary_diagonal = 0

for i in range(n):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][- (i + 1)]

print(abs((primary_diagonal - secondary_diagonal)))