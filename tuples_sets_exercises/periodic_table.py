n_count=int(input())

result_set = set()

for _ in range(n_count):
    data=set(input().split(' '))
    result_set = result_set | data

for item in result_set:
    print(item)
