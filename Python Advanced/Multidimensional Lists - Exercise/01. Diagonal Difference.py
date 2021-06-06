def create_matrix(num):
    matrix = []
    for _ in range(num):
        matrix.append([int(el) for el in input().split()])
        
    return matrix


n = int(input())

matrix = create_matrix(n)
sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for row in range(n):
    sum_primary_diagonal += matrix[row][row]

# row = 0
# for col in range(n-1, -1, -1):
#     sum_secondary_diagonal += matrix[col][row]
#     row += 1

for i in range(n):
    sum_secondary_diagonal += matrix[len(matrix) - 1 -i][i]

print(abs(sum_secondary_diagonal - sum_primary_diagonal))
