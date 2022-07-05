import re

with open('words.txt') as words_fh:
    words = words_fh.read().split()

with open('input.txt') as input_fh:
    text = input_fh.read()

word_ocurrences={}



for word in words:
    matches=re.findall(rf'[\s?!-]({word})[\s.?!,]', text, re.MULTILINE + re.IGNORECASE)
    word_ocurrences[word.lower()]=len(matches)

with open('output.txt', 'w') as output_fh:
    for word, occurences in sorted(word_ocurrences.items(), key=lambda t: -t[1]):
        print(f"{word} - {occurences}", file=output_fh)