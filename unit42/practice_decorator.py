def type_check(x, y):
    def real_decorator(func):
        def wrapper(a, b):
            r = func(a, b)
            if type(a) is not x or type(b) is not y:
                raise RuntimeError('자료형이 올바르지 않습니다.')
            return r
        return wrapper
    return real_decorator


@type_check(int, int)
def add(a, b):
    return a + b


print(add(10, 20))
print(add('hello', 'world'))
