def calc():
    result = None
    while True:
        expression = (yield result)
        split_exp = expression.split()
        if split_exp[1] == '+':
            result = int(split_exp[0]) + int(split_exp[2])
        elif split_exp[1] == '-':
            result = int(split_exp[0]) - int(split_exp[2])
        elif split_exp[1] == '*':
            result = int(split_exp[0]) * int(split_exp[2])
        elif split_exp[1] == '/':
            result = int(split_exp[0]) / int(split_exp[2])


expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
