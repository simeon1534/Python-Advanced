command = input()
inp = list(map(int, input().split(' ')))

odd_sum = sum(list(filter(lambda x: x % 2 != 0, inp)))
even_sum = sum(list(filter(lambda x: x % 2 == 0, inp)))

if command == 'Odd':
    print(odd_sum * len(inp))
elif command == 'Even':
    print(even_sum * len(inp))
