from collections import deque


def read_matrix():
    rows, cols = [int(n) for n in input().split(' ')]
    matrix = [
        [0 for n in range(cols)]
        for _ in range(rows)
    ]
    return matrix


def reverse_order(matrix, i):
    if i % 2 != 0:
        return matrix[i].reverse()


def filling_rows(matrix, snake):
    snake_left = deque(list(snake))
    # print(snake_left)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = snake_left.popleft()
            if not snake_left:
                snake_left = deque(list(snake))
        reverse_order(matrix, i)
        # print(matrix)
    return matrix


matrix = read_matrix()
snake = input()
result = filling_rows(matrix, snake)
print('\n'.join(''.join(row) for row in result))
