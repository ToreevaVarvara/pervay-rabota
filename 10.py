with open('matrix.txt', 'r') as file:
    matrix = []
    for line in file:
        row = list(map(int, line.split()))  # Преобразуем строки в списки целых чисел
        matrix.append(row)

for row in matrix:
    row.sort()

with open('sorted_matrix.txt', 'w') as file:
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')

print("Матрица отсортирована и записана в 'sorted_matrix.txt'.")
