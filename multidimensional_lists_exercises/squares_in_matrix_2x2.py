def read_matrix():
    rows, cols = [int(n) for n in input().split(' ')]
    matrix = [
        [n for n in input().split(' ')]
        for _ in range(rows)
    ]
    return matrix


def getting_square(matrix):
    squares = 0
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]],
            ]
            if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                squares += 1
    return squares

matrix = read_matrix()
result = getting_square(matrix)
print(result)
