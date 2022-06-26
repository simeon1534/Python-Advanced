sequence_username=int(input())

collection=set()

for _ in range(sequence_username):
    username=input()
    collection.add(username)

for item in collection:
    print(item)