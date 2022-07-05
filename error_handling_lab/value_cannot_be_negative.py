class NegativeError(Exception):
    pass


for i in range(1, 6):
    num = int(input())
    if num < 0:
        raise NegativeError
