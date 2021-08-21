def file_read():
    with open('./unit40/words.txt') as file:
        for word in file:
            yield word


for i in file_read():
    print(i)
