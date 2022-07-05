from collections import deque

duration_green = int(input())
duration_free_window = int(input())  # kogato svyrshi zelenoto se gleda
queue = deque()
crossroad = deque()  # kakva chast ot kolata e preminala krystovisheteto  #deque????

safe_cars = 0
command = input()
while not command == 'END':
    if command == 'green':  # opashkata zapochva da minava dokato ne izteche zelenoto
        timer = duration_green
        for car in queue.copy():
            timer=timer-len(car)

            if timer<0:
                car_part=car[timer:]
                #print(car_part)
                if duration_free_window+timer>=0: #uspeh
                    safe_cars+=1
                    queue.popleft()

                else:
                    print('A crash happened!')
                    print(f"{car} was hit at {car[duration_free_window+timer]}.")
                    exit()
            elif timer==0:
                queue.popleft()
                safe_cars += 1
                break
            elif timer>0:
                queue.popleft()
                safe_cars+=1


    else:
        car = command
        queue.append(car)  # ako komandata e kola dobavqme na opashka
    command = input()
#
print(f"Everyone is safe.")
print(f"{safe_cars} total cars passed the crossroads.")
exit()
