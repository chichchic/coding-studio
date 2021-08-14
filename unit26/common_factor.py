def set_factor(num):
    return {i for i in range(1, num + 1) if num % i == 0}


input_a, input_b = list(map(int, input().split()))
a = set_factor(input_a)
b = set_factor(input_b)

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
