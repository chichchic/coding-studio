x, y = map(int, input().split())


def calc(val1, val2):
    return val1 + val2, val1 - val2, val1 * val2, val1/val2


a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
