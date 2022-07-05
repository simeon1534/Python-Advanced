from collections import deque


def loading_gun(bullets, size_gun_barrel):
    bullets_pistol = []
    for i in range(1, size_gun_barrel + 1):
        if len(bullets) > 0:
            bullets_pistol.append(bullets.pop())
    return bullets_pistol


price_per_bullet = int(input())
size_gun_barrel = int(input())

bullets_all = input().split(' ')
locks = deque(input().split(' '))
bullets = [int(b) for b in bullets_all]  # stack
locks = deque([int(l) for l in locks])

price = int(input())

razhod = 0
left_bullets = size_gun_barrel
bullets_pistol = deque(loading_gun(bullets, size_gun_barrel))  # queue

while len(bullets) + len(bullets_pistol) > 0 and len(locks) > 0:
    if bullets_pistol[0] <= locks[0]:  # shcupva kluchalka - BANG
        locks.popleft()  # maham kluchalka
        print('Bang!')
    elif bullets_pistol[0] > locks[0]:  # ne schupva kluchalka - PING
        print('Ping!')  # ne maham kluchalka

    bullets_pistol.popleft()  # maham bullet ot pylnitelq
    left_bullets -= 1
    razhod += price_per_bullet
    if left_bullets == 0 and len(bullets) > 0:  # Reloading
        print('Reloading!')
        left_bullets = size_gun_barrel
        bullets_pistol = deque(loading_gun(bullets, size_gun_barrel))  # queue

if len(locks) > 0:  # FAIL
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets) + len(bullets_pistol)} bullets left. Earned ${price - razhod}")
