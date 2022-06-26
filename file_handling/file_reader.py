f = open('numbers.txt')
total=0
for line in f:
    n = int(line.strip())
    total+=n
print(total)