def countdown(n):
    count = n + 1

    def do_countdown():
        nonlocal count
        count -= 1
        return count
    return do_countdown


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')
