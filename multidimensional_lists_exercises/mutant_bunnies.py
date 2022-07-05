from collections import deque


def read_matrix():
    rows, cols = [int(n) for n in input().split(' ')]
    matrix = [
        [j for j in input()]
        for i in range(rows)
    ]
    return matrix


def is_in_range(row, col, matrix_row_length, matrix_col_length):
    if 0 <= row < matrix_row_length and 0 <= col < matrix_col_length:
        return True
    return False


def multiplying(matrix):
    list_bunnies = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "B":
                list_bunnies.append([i, j])  # dobavqme koordinati na zaicite
    for coordinates in list_bunnies:
        i, j = coordinates
        tuple_posoki = (
            (i + (-1), j),
            (i + 1, j),
            (i, j + 1),
            (i, j + (-1))
        )
        for posoka in tuple_posoki:
            new_row, new_col = posoka
            if is_in_range(new_row, new_col, len(matrix), len(matrix[0])):
                if matrix[new_row][new_col] == '.':
                    matrix[new_row][new_col] = 'B'
                elif matrix[new_row][new_col] == 'P':
                    # lose
                    matrix[new_row][new_col] = 'B'
                    print('\n'.join(''.join(row) for row in matrix))
                    print(f"dead: {new_row} {new_col}")
    return matrix


directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}
matrix = read_matrix()
commands = deque(list(input()))
while commands:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "P":
                if commands:
                    command = commands.popleft()
                    new_row = i + directions[command][0]
                    new_col = j + directions[command][1]
                    if is_in_range(new_row, new_col, len(matrix), len(matrix[0])):
                        # move
                        if matrix[new_row][new_col] == '.':
                            matrix[i][j] = '.'
                            matrix[new_row][new_col] = 'P'
                        elif matrix[new_row][new_col] == 'B':
                            # lose
                            matrix[i][j] = '.'
                            multiplying(matrix)
                            print('\n'.join(''.join(row) for row in matrix))
                            print(f"dead: {new_row} {new_col}")

                    else:
                        # WIN
                        matrix[i][j] = '.'
                        multiplying(matrix)
                        print('\n'.join(''.join(row) for row in matrix))
                        print(f"won: {i} {j}")
                    multiplying(matrix)
