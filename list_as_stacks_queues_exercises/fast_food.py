from collections import deque

food_quantity=int(input())

orders=deque(input().split(' '))
max_done_orders = max([int(o) for o in orders])
print(max_done_orders)
done_orders=[]
fail=False
for i in range(len(orders)):
    if food_quantity-int(orders[0])>=0:
        food_quantity-=int(orders[0])
        removed=orders.popleft()
        done_orders.append(removed)
    else:
        print(f"Orders left: {' '.join(orders)}")
        fail=True
        break

if not fail:
    print(f"Orders complete")
