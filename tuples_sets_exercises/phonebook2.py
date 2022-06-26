nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dictionary = {}
data = input()
while data not in nums:
    name, phone = data.split('-')
    dictionary[name] = phone
    data = input()
last_data = data

for _ in range(int(last_data)):
    name=input()
    if name in dictionary:
        print(f"{name} -> {dictionary[name]}")
    else:
        print(f"Contact {name} does not exist.")