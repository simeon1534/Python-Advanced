def read_matrix():
    n = int(input())
    matrix = [list(map(int,input().split())) for row in range(n)]
    return matrix


def is_in_range(matrix, row, col):
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:
        return True
    print("Invalid coordinates")
    return False


def add(matrix, row, col, value):
    if is_in_range(matrix, row, col):
        matrix[row][col] += value


def subtract(matrix, row, col, value):
    if is_in_range(matrix, row, col):
        matrix[row][col] -= value



matrix = read_matrix()

data=input()
while not data=="END":
    command,row,col,value=data.split()
    row=int(row)
    col=int(col)
    value=int(value)

    if command=="Add":
        add(matrix, row, col, value)
    elif command=="Subtract":
        subtract(matrix, row, col, value)
    data = input()

print('\n'.join([' '.join(list(map(str,row))) for row in matrix]))
