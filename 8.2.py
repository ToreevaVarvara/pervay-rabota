matrix = np.array([
    [3.5, 1.2, 2.4, 5.1],
    [9.0, 7.3, 8.6, 4.2],
    [5.5, 4.0, 6.1, 0.0]
])
new_matrix = np.copy(matrix)
for i in range(new_matrix.shape[0]):
    min_index = np.argmin(new_matrix[i])
    min_value = new_matrix[i][min_index]
    if min_value % 2 == 0:
        new_matrix[i][min_index] = 0
    else:
        new_matrix[i][min_index] = 1
print("Новая матрица:")
print(new_matrix)
