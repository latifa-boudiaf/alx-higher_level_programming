#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[j])):
            row.append(matrix[i][j] ** 2)
        
        new_matrix.append(row)

    return new_matrix

