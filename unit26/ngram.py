def ngram(word, n):
    list = []
    for i in range(len(word)-n+1):
        list.append(word[i:i+n])
    return list


print(ngram("abcdefghijklmnopqrstuvwxyz", 3))
