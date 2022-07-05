text = input()
try:
    times = int(input())
    for i in range(times):
        print(text, end='')
except ValueError:
    print("Variable times must be an integer")
