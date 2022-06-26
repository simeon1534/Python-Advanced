sequence_integers=input().split(' ')
capacity_stack=int(input())

stack=[int(s) for s in sequence_integers]
racks=0
new_rack=[]
#print(stack)
while len(stack)>0:
    new_rack.append(stack.pop())
    if sum(new_rack)>capacity_stack:
        racks+=1
        za_sledvashtiq_rack=new_rack.pop()
        new_rack.clear()
        new_rack.append(za_sledvashtiq_rack)
    elif sum(new_rack)==capacity_stack:
        racks += 1
        new_rack.clear()
if len(new_rack)>0:
    racks+=1

print(racks)