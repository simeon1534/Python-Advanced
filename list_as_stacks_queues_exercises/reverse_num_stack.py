nums=input().split()

stack=[]
for num in nums:
    stack.append(num)

reversed=[]
while len(stack)>0:
    for_reversed=stack.pop()
    reversed.append(for_reversed)
print(*reversed)