item_categories = input().split(", ")
lines = int(input())

dictionary = {category: list() for category in item_categories}

quantity = 0
quality = 0
for i in range(lines):
    # food - pizza - quantity: 10;quality: 5
    category, item, qua = input().split(" - ")
    dictionary[category].append(item)

    curr_quantity, curr_quality = qua.split(';')

    quantity += int(curr_quantity.split(':')[1])
    quality += int(curr_quality.split(':')[1])

print(f"Count of items: {quantity}")
print(f"Average quality: {quality/len(dictionary):.2f}")
for category in dictionary:
    print(f"{category} -> {', '.join(dictionary[category])}")
    
# Count of items: 25
# Average quality: 8.00
# food -> pizza, burgers
# water -> mineral
# materials -> wood
# metal -> copper
