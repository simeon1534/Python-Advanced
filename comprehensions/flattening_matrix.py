#n=int(input())

#matrix=[[int(n) for n in input().split(', ')]for _ in range(n)]
#flat_matrix=[number for row in matrix for number in row]
#print(flat_matrix)

print(int(n) for _ in range(int(input())) for n in input().split(', '))