s, e = list(map(int, input().split()))
answer = [pow(2, num + s)
          for num in range(e - s + 1) if num != 1 and num != e - s - 1]
print(answer)
