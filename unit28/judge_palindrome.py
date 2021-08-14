def palindrome(word):
    is_palindrome = True
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            is_palindrome = False
            break
    return is_palindrome


with open('./unit28/words.txt', 'r') as file:
    for word in [s for s in file if palindrome(s.strip('\n'))]:
        print(word.strip('\n'))
