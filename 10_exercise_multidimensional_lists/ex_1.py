
n = int(input())
matrix = [[int(x) for x in input().split(', ')] for r in range(n)]

diagonal = []
opp_diagonal = []

for i in range(n):
    diagonal.append(matrix[i][i])
    opp_diagonal.append(matrix[i][- (i + 1)])

print(f'Primary diagonal: {", ".join(map(str, diagonal))}. Sum: {sum(diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, opp_diagonal))}. Sum: {sum(opp_diagonal)}')
