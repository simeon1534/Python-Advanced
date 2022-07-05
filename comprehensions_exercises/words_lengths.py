#names=input().split(', ')

#for name in names:
 #   print(f"{name} -> {len(name)}",end=', ')

print(', '.join([f"{name} -> {len(name)}" for name in input().split(', ')]))
