with open('./unit27/words.txt', 'r') as file:
    count = len([s for s in file if len(s.strip('\n')) <= 10])
    print(count)
