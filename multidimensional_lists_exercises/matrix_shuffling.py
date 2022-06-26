def swap_val(matrix, row1, col1, row2, col2):
    if row1 < len(matrix) and row2 < len(matrix) and col1 < cols and col2 < cols:
        temp = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = temp
        return '\n'.join([' '.join(map(str, row)) for row in matrix])
    else:
        return 'Invalid input!'


rows, cols = [int(n) for n in input().split(' ')]
matrix = [
    [n for n in input().split(' ')]
    for _ in range(rows)
]

data = input()
while data != 'END':
    try:
        command, row1, col1, row2, col2 = data.split(' ')
        row1 = int(row1)
        row2 = int(row2)
        col1 = int(col1)
        col2 = int(col2)
        if command == 'swap':
            print(swap_val(matrix, row1, col1, row2, col2))
    except ValueError:
        print('Invalid input!')
    data = input()
