from functools import reduce


# operation=lambda operator,*args :
def operate(op, *args):
    if op == '+':
        return reduce(lambda a, b: a + b, args,0)
    if op == '-':
        return reduce(lambda a, b: a - b, args,0)
    if op == '/':
        return reduce(lambda a, b: a / b, args,1)
    if op == '*':
        return reduce(lambda a, b: a * b, args,1)

print(operate('/',1,2,3))
