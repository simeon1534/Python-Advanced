from collections import deque

sequence_of_parentheses = input()
sequence_of_parentheses=sequence_of_parentheses.replace(" ","")
sequence_of_parentheses = list(sequence_of_parentheses)

stack_otvarqshti = []
queue_zatvarqshti = deque()
# print(sequence_of_parentheses)
polovina = len(sequence_of_parentheses) / 2
for i in range(int(polovina)):
    stack_otvarqshti.append(sequence_of_parentheses[i])
# print(stack_otvarqshti)
for i in range(int(polovina), len(sequence_of_parentheses)):
    queue_zatvarqshti.append(sequence_of_parentheses[i])
# print(queue_zatvarqshti)

balanced = True
while len(stack_otvarqshti) > 0 and len(queue_zatvarqshti) > 0:

    if stack_otvarqshti[-1] == '(' and queue_zatvarqshti[0] == ')':
        stack_otvarqshti.pop()
        queue_zatvarqshti.popleft()


    elif stack_otvarqshti[-1]== '[' and queue_zatvarqshti[0] == ']':
        stack_otvarqshti.pop()
        queue_zatvarqshti.popleft()


    elif stack_otvarqshti[-1]== '{' and queue_zatvarqshti[0] == '}':
        stack_otvarqshti.pop()
        queue_zatvarqshti.popleft()


    elif stack_otvarqshti[-1] == ' ' and queue_zatvarqshti[0] == ' ':
        stack_otvarqshti.pop()
        queue_zatvarqshti.popleft()


    else:
        balanced = False
        break

if balanced:
    print('YES')
else:
    print('NO')
