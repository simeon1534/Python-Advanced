from datetime import datetime, timedelta
from collections import deque

dict = {}
queue = deque()

# dictionary with robots name as key and processing time as value
robots_processing = input().split(';')
for robot_process in robots_processing:
    robot, process = robot_process.split('-')
    dict[robot] = process
# print(dict)

cooldown = {el: 0 for el in dict}
# print(cooldown)
# dictionary pokazvashto dali robotite sa v cooldown ili sa svobodni(ako value e 0)

# izchislqvane na vreme
start_time = datetime.strptime(input(), '%H:%M:%S')

current_time = 0

# cooldown={}


data = input()
while not data == 'End':
    queue.append(data)
    data = input()
while len(queue) > 0:
    current_time += 1

    # vreme za izchakvane na roboti -1 sekunda ,ako stane 0 sa nalicni
    for robot in cooldown:
        if cooldown[robot] == 0:
            continue
        else:
            cooldown[robot] -= 1

    is_processed = False

    # proverka za nalichen robot
    for robot in dict:
        if cooldown[robot] == 0:
            cooldown[robot] = int(dict[robot])
            time_str = (start_time + timedelta(seconds=current_time)) \
                .strftime('%H:%M:%S')
            print(f"{robot} - {queue[0]} [{time_str}]")
            queue.popleft()

            is_processed = True
            break
    # algoritym za produkt minavane otzade na opashkata ako nqma koi da go obrabotva
    if not is_processed:
        queue.append(queue.popleft())

#  NE RABOTI
# ROB-1000000;SS2-100000;NX8000-1000000
# 23:59:58
# detail
# glass
# wood
# apple
# End
