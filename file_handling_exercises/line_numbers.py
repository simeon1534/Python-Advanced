import re

with open('text.txt', 'r') as text_fh:
    text = text_fh.readlines()
    pattern_letters = r'[A-Za-z0-9]'
    pattern_punc = r'[^\w\s]'
    pattern_punc_under = r'_'

    for line in text:
        match = re.findall(pattern_letters, line)
        match_punc = re.findall(pattern_punc, line)
        match_punc_under = re.findall(pattern_punc_under, line)
        with open('output.txt', 'a') as output_fh:
            print(f"Line {text.index(line) + 1}: {line} ({len(match)})({len(match_punc) + len(match_punc_under)})",
                  file=output_fh)
