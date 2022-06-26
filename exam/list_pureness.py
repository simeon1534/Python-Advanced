from collections import deque

test = ([1, 2, 3, 4, 5], 10)
def best_list_pureness(*args):
    original_list, rotations = args
    original_list = deque(original_list)
    dict_pureness = []
    for rotation in range(rotations + 1):
        list_pureness = 0
        for i in range(len(original_list)):
            list_pureness += original_list[i] * i
        dict_pureness.append([list_pureness, rotation])  # zapisvane na rezultata
        original_list.appendleft(original_list.pop())  # smqna na reda

    best_pureness = [0, 0]

    for el in dict_pureness:
        pureness, rotation = el
        if pureness > best_pureness[0]:
            best_pureness[0] = pureness
            best_pureness[1] = rotation
    res = f"Best pureness {best_pureness[0]} after {best_pureness[1]} rotations"
    return res


print(best_list_pureness(*test))
