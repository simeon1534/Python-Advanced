def palindrome(word, index):

    if len(word) < 3:
        return word
    if word[0] == word[-1]:
        return palindrome(word,index)+palindrome(word[1:-1], index + 1)



print(palindrome("abcba", 0))
print(palindrome("peter", 0))