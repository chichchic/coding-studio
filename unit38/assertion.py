x = int(input('3의 배수를 입력하세요: '))
# 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감. 디버깅 모드에서만 실행된다.
assert x % 3 == 0, '3의 배수가 아닙니다.'
print(x)
