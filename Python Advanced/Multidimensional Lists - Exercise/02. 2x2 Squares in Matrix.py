def create_matrix(num1, num2):
    sublist = []
    for i in range(num1):
        sublist.append([el for el in input().split()])
        
    return sublist


rows, cols = input().split()

rows, cols = int(rows), int(cols)
matrix = create_matrix(rows, cols)

all_match = 0

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            all_match += 1

print(all_match)
