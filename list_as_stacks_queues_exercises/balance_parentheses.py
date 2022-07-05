PAIRINGS = {
    '(': ')',
    '{': '}',
    '[': ']'
}
sequence_of_parentheses = input()


def is_balanced(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  # too many closing symbols
            return False
        if s != PAIRINGS[expected_opening_symbol]:  # mismatch
            return False
    return len(stack) == 0  # false if too many opening symbols

if is_balanced(sequence_of_parentheses):
    print('YES')
else:
    print('NO')

