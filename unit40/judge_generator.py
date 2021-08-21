def prime_number_generator(start, stop):
    current = start
    prime_list = [2]
    if start != 0:
        prime_list = [i for i in prime_number_generator(0, start - 1)]

    if start <= 2:
        yield 2
        current = 3
    while current <= stop:
        is_prime = True
        for prime in prime_list:
            if current % prime is 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(current)
            yield current
        current += 1


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
