# n = int(input())

print([[int(n) for n in input().split(', ') if int(n) % 2 == 0] for _ in range(int(input()))])
# print(matrix)
#print(int(n) for _ in range(int(input())) for n in input().split(', ') if int(n) % 2 == 0)
