set1_length,set2_length=map(lambda x: int(x), input().split(' '))

set1=set()
for _ in range(set1_length):
    data=int(input())
    set1.add(data)

set2=set()
for _ in range(set2_length):
    data=int(input())
    set2.add(data)

result_set=set1 & set2
for item in result_set:
    print(item)


