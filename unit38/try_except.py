try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except ZeroDivisionError as e:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:    # 예외가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.', e)
