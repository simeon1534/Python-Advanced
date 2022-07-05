item_categories = input().split(", ")
lines = int(input())

dictionary = {category: dict() for category in item_categories}


for i in range(lines):
    # {food : {pizza : {quantity: 10,quality: 5}},burger : {quantity:5 , quality:2}}
    category, item, qua = input().split(" - ")
    curr_quantity, curr_quality = qua.split(';')
    dictionary[category][item]={curr_quantity.split(':')[0]:int(curr_quantity.split(':')[1]),curr_quality.split(':')[0]:int(curr_quality.split(':')[1])}

print(sum([dictionary[category][item]['quantity'] for category in dictionary for item,dict_quality_quantity in dictionary[category].items()]))
print(f"Average quality: {sum([dictionary[category][item]['quality'] for category in dictionary for item,dict_quality_quantity in dictionary[category].items()]) / len(dictionary):.2f}")
print(dictionary)
for category in dictionary:
     print(f"{category} -> {', '.join(dictionary[category])}")

# Count of items: 25
# Average quality: 8.00
# food -> pizza, burgers
# water -> mineral
# materials -> wood
# metal -> copper
