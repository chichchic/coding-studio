from functools import reduce


def plus_ten(x): return x + 10  # plus_ten = lambda x: x + 10


print((lambda x: x + 10)(10))
print(list(map(lambda x: x + 10, [1, 2, 3])))

# 반듯이 else를 사용해야만 함
print(list(map(lambda x: x if x % 3 == 0 else None, [1, 2, 3, 4, 5])))
print(list(map(lambda x, y: x * y, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])))

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
