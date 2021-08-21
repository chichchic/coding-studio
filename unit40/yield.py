def number_generator():
    yield 0
    yield 1
    yield 2


for i in number_generator():
    print(i)

g = number_generator()

a = next(g)    # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)       # 0

b = next(g)
print(b)       # 1

c = next(g)
print(c)       # 2
