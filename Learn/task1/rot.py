matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# roll the indexes of elements by 1 position
rolled_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        rolled_matrix[i][(j+1) % len(matrix)] = matrix[i][j]

print(rolled_matrix)