from collections import deque

cups_capacity_str=input().split(' ')
filled_bottles_str=input().split(' ')

cups_capacity=deque([int(c) for c in cups_capacity_str])    #queue
filled_bottles=[int(b) for b in filled_bottles_str]    #stack

wasted_water=0
while len(cups_capacity)>0 and len(filled_bottles)>0:
    res=filled_bottles.pop()-cups_capacity[0]
    if res<0:
        #namalqme cup capacity
        cups_capacity[0]=-res
    else:   #izlishna voda
        wasted_water+=res
        cups_capacity.popleft()
if len(cups_capacity)>0: #ostavat nenapylneni chashi
    joined_cups = ' '.join([str(c) for c in cups_capacity])
    print(f"Cups: {joined_cups}")
    print(f"Wasted litters of water: {wasted_water}")
else: #napylvame vsichki chashi =>len(cups_capacity)==0
    joined_bottles = ' '.join([str(b) for b in filled_bottles])
    print(f"Bottles: {joined_bottles}")
    print(f"Wasted litters of water: {wasted_water}")