def palindrome(word):
    return word.lower()==word.lower()[::-1]

print(palindrome("Potop"))