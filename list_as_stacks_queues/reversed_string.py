string=input()
stack=[]

for char in string:
    stack.append(char)

reversed=''

while len(stack)>0:
    item=stack.pop()
    reversed+=item

print(reversed)