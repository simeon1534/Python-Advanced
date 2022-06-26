names = input().split(", ")

dictionary = {name: set() for name in names}
cost_dict={name:0 for name in names}

data = input()
while not data == "End":
    name, item, cost = data.split("-")
    if item not in dictionary[name]:
        cost_dict[name] += int(cost)
    dictionary[name].add(item)
    data = input()

for name in dictionary:
    print(f"{name} -> Items: {len(dictionary[name])}, Cost: {cost_dict[name]}")