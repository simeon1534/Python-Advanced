from itertools import chain


# square 3x3
def read_matrix():
    rows, cols = [int(n) for n in input().split(' ')]
    matrix = [
        [int(n) for n in input().split(' ')]
        for _ in range(rows)
    ]
    return matrix


def get_squares(matrix):
    cols=0
    for row in matrix:
        cols+=1
    squares = []
    row = matrix[0]
    for i in range(cols-2):
        for j in range(len(row)-2):
            square = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
            ]
            squares.append(square)
    return squares


def get_sum_of_matrix(matrix):
    return sum(chain(*matrix))


def get_max_square(squares):
    max_square = None
    max_square_sum = None
    for square in squares:
        square_sum = get_sum_of_matrix(square)
        if max_square_sum is None or square_sum > max_square_sum:
            max_square_sum = square_sum
            max_square = square
    return max_square


matrix = read_matrix()
squares = get_squares(matrix)
max_square = get_max_square(squares)
print(f"Sum = {get_sum_of_matrix(max_square)}")
print('\n'.join([' '.join(map(str, row)) for row in max_square]))
