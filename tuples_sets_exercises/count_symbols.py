sequence=input()
dictionary_letters = {}
for letter in sequence:
    if letter not in dictionary_letters:
        dictionary_letters[letter] = 1
    else:
        dictionary_letters[letter] += 1

ordered_dict=sorted(dictionary_letters.items())

for letter,count in ordered_dict:
    print(f"{letter}: {count} time/s")

