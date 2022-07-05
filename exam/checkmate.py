def finding_king(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'K':
                coord = [i, j]
                return coord


def is_in_range(matrix, row_index, col_index):
    if row_index > len(matrix) - 1 or row_index < 0:
        return False
    elif col_index > len(matrix) - 1 or col_index < 0:
        return False
    else:
        return True


def path_clear_horizontal(matrix, q_coord, king_coord):
    row_q, col_q = q_coord
    row_king, col_king = king_coord
    if col_q > col_king:
        for area in range(col_q - 1, col_king, -1):  # K . . . Q
            if matrix[row_q][area] == 'Q':
                return False
        return True
    else:
        for area in range(col_q + 1, col_king):  # Q . . . K
            if matrix[row_q][area] == 'Q':
                return False
        return True


def path_clear_vertical(matrix, q_coord, king_coord):
    row_q, col_q = q_coord
    row_king, col_king = king_coord
    if row_q > row_king:
        for area in range(row_q - 1, col_king, -1):  # K . . . Q
            if matrix[area][col_q] == 'Q':
                return False
        return True
    else:
        for area in range(row_q + 1, row_king):  # Q . . . K
            if matrix[area][col_q] == 'Q':
                return False
        return True


def path_clear_diagonal(matrix, q_coord, king_coord):
    row_q, col_q = q_coord
    row_king, col_king = king_coord
    if row_q < row_king and col_q < col_king:  # 1
        counter = 1
        for area in range(row_q + 1, row_king):
            if matrix[area][col_q + counter] == 'Q':
                return False
            counter += 1
        return True

    if row_q > row_king and col_q < col_king:  # 2
        counter = row_q - 1
        for area in range(col_q + 1, col_king):
            if matrix[counter][area] == 'Q':
                return False
            counter -= 1
        return True

    if row_q < row_king and col_q > col_king:  # 3
        counter = row_q + 1
        for area in range(col_q - 1, col_king, -1):
            if matrix[counter][area] == 'Q':
                return False
            counter += 1
        return True

    if row_q > row_king and col_q > col_king:  # 4
        counter = 1
        for area in range(row_q - 1, row_king, -1):
            if matrix[area][col_q - counter] == 'Q':
                return False
            counter += 1
        return True


matrix = []
q = 0

for i in range(7):
    matrix.append(input().split())

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'Q':

            if 'K' in matrix[i]:
                if path_clear_horizontal(matrix, [i, j], finding_king(matrix)):
                    print(f"[{i}, {j}]")
                    q += 1  # king dies
            for row in matrix:
                if row[j] == 'K' and path_clear_vertical(matrix, [i, j], finding_king(matrix)):
                    print(f"[{i}, {j}]")
                    q += 1  # king dies

            counter = 1
            while True:
                if is_in_range(matrix, i + counter, j + counter):
                    if matrix[i + counter][j + counter] == 'K':
                        if path_clear_diagonal(matrix, [i, j], finding_king(matrix)):
                            print(f"[{i}, {j}]")

                            q += 1  # king dies
                    counter += 1
                else:
                    break

            counter = 1
            while True:
                if is_in_range(matrix, i + counter, j - counter):
                    if matrix[i + counter][j - counter] == 'K':
                        if path_clear_diagonal(matrix, [i, j], finding_king(matrix)):
                            print(f"[{i}, {j}]")

                            q += 1  # king dies
                    counter += 1
                else:
                    break

            counter = 1
            while True:
                if is_in_range(matrix, i - counter, j + counter):
                    if matrix[i - counter][j + counter] == 'K':
                        if path_clear_diagonal(matrix, [i, j], finding_king(matrix)):
                            print(f"[{i}, {j}]")

                            q += 1  # king dies
                    counter += 1
                else:
                    break

            counter = 1
            while True:
                if is_in_range(matrix, i - counter, j - counter):
                    if matrix[i - counter][j - counter] == 'K':
                        if path_clear_diagonal(matrix, [i, j], finding_king(matrix)):
                            print(f"[{i}, {j}]")

                            q += 1  # king dies
                    counter += 1
                else:
                    break
if q == 0:
    print('The king is safe!')
