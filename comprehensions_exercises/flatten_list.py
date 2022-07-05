string = "".join(reversed(input())).split('|')

res = ' '.join([el for m in string for el in m if el != ' '])
# for m in string:
#     res.append(m.split(' '))
print(string)
print(res)
