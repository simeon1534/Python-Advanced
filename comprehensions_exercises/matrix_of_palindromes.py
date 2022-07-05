import string
alphabet_list = list(string.ascii_lowercase)
inp=list(map(int,input().split()))

matrix=[alphabet_list[i]+alphabet_list[j+i]+alphabet_list[i] for i in range(inp[0]) for j in range(inp[1])]

print(matrix)