from collections import deque
petrol_pumps=int(input())

right_start=deque()
index=0

for i in range(petrol_pumps):
    liter,km=input().split(' ')
    right_start.append([liter,km])
for i in range(petrol_pumps):
    for_next_path=0
    for path in right_start:
        liter=int(path[0])
        km=int(path[1])
        ostatyk=(liter-km)+for_next_path
        if ostatyk<0:
            right_start.append(right_start.popleft())
            index+=1
            break
        for_next_path=ostatyk
print(index)
