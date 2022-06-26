n_queries=int(input())

stack=[]

for i in range(n_queries):
    command=input().split()
    if len(command)>1 and command[0]=='1':
        element=int(command[1])
        if 1 <= element <= 109:
            stack.append(element)
    elif command[0]=='2':
        if len(stack)>0:
            stack.pop()

    elif command[0]=='3':
        if len(stack) > 0:
            print(max(stack))
    elif command[0]=='4':
        if len(stack) > 0:
            print(min(stack))
stack.reverse()
new_stack = ', '.join(str(v) for v in stack)
print(new_stack)

