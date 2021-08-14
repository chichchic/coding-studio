def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환


c = calc()
print(c(1), c(2), c(3), c(4), c(5))


def calc2():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환


c2 = calc()
print(c2(1), c2(2), c2(3), c2(4), c2(5))
