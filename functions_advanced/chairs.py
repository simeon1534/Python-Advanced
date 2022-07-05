import itertools

prople=input().split(', ')
n=int(input())

for combination in itertools.combinations(prople,n):
    print(', '.join(combination))