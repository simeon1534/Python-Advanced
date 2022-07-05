inp = list(map(int,input().split(' ')))
filtering = list(filter(lambda x: x % 2 == 0, inp))
print(filtering)
