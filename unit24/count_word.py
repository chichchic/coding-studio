import string


def count_word(paragraph, word):
    paragraph = list(map(lambda s: s.strip(
        string.punctuation), paragraph.split()))
    return paragraph.count(word)


paragraph = input()
print(count_word(paragraph, 'the'))
