import numpy as np
def modify_matrix(matrix):
    if not isinstance(matrix, np.ndarray):
        return None
rows, cols = matrix.shape
new_matrix = np.copy(matrix) 
for i in range(rows):
        min_val = min(matrix[i])
        min_index = matrix[i].tolist().index(min_val)
        if min_val % 2 == 0:
            new_matrix[i][min_index] = 0
        else:
            new_matrix[i][min_index] = 1
return new_matrix
