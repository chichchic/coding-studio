with open('./unit27/words.txt', 'r') as file:
    line = file.readline()
    for answer in [s for s in line.split() if 'c' in s]:
        print(answer.strip(',.'))
