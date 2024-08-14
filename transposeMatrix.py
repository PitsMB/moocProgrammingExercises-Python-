# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

# Write your solution here

def transpose(matrix: list):
    # original = [row.copy() for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                break
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    

if __name__ == "__main__":
    my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed_matrix = transpose(my_list)
    print(transposed_matrix)