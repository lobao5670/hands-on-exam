def palindrome(word):
    word = word.lower().replace(' ', '')
    reverse = ''.join(reversed(word))
    print(word == reverse)

word = 'A lupa  pula'
palindrome(word)