n=int(input())
names=set()

for _ in range(n):
    command,id=input().split(', ')
    if command=='IN':
        names.add(id)
        #print(id)
    elif command=='OUT':
        names.remove(id)

if len(names)>0:
    for name in names:
        print(name)
else:
    print('Parking Lot is Empty')