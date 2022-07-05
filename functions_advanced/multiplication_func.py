from functools import reduce
multiply = lambda *args: reduce(lambda a, b: a * b, args)
print(multiply(1,2,3,4,5))
def mult(*args):
    return reduce(lambda a, b: a * b, args)

print(mult(1,2,3,4,5))