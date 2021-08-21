import random

for i in iter(lambda: random.randint(0, 5), 2):
    print(i, end=' ')
