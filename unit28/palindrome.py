def palindrome(word):
    is_palindrome = True
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            is_palindrome = False
            break

    if(is_palindrome):
        print('is palindrome')
    else:
        print('is not palindrome')


palindrome("121")
