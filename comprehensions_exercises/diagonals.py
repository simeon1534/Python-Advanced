n = int(input())

matrix = [input().split(', ') for i in range(n)]

first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][-i-1] for i in range(n)]
print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum([int(matrix[i][i]) for i in range(n)])}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum([int(matrix[i][-i-1]) for i in range(n)])}")
