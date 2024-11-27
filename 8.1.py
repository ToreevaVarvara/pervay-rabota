import numpy as np
matrix = np.array([[3, 1, 2],
                   [9, 7, 8],
                   [5, 4, 6]])
sorted_matrix = np.array([np.sort(row) for row in matrix])
print("Исходная матрица:")
print(matrix)
print("\nОтсортированная матрица:")
print(sorted_matrix)
