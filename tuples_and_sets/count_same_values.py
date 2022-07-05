from collections import defaultdict

d=defaultdict(int)
numbers=map(float,input().split(' '))

for number in numbers:
    d[number]+=1

for number,occurrence_count in d.items():
    print(f"{number} - {occurrence_count} times")