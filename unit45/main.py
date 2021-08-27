# import person    # import로 person 모듈을 가져옴
# import square2               # import로 square2 모듈을 가져옴

# print(square2.base)          # 모듈.변수 형식으로 모듈의 변수 사용
# print(square2.square(10))    # 모듈.함수() 형식으로 모듈의 함수 사용


# # 모듈.클래스()로 person 모듈의 클래스 사용
# maria = person.Person('마리아', 20, '서울시 서초구 반포동')
# maria.greeting()

# import hello    # hello 모듈을 가져옴. 파이썬은 모듈을 가져올 경우 스크립트 파일이 한번 실행된다.

# print('main.py __name__:', __name__)    # __name__ 변수 출력

# import calc

# print(calc.add(50, 60))
# print(calc.mul(50, 60))

# import calcpkg.operation    # calcpkg 패키지의 operation 모듈을 가져옴
# import calcpkg.geometry     # calcpkg 패키지의 geometry 모듈을 가져옴

# print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
# print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용

# # geometry 모듈의 triangle_area 함수 사용
# print(calcpkg.geometry.triangle_area(30, 40))
# # geometry 모듈의 rectangle_area 함수 사용
# print(calcpkg.geometry.rectangle_area(30, 40))

# import calcpkg    # calcpkg 패키지만 가져옴

# print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
# print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용

# # geometry 모듈의 triangle_area 함수 사용
# print(calcpkg.geometry.triangle_area(30, 40))
# # geometry 모듈의 rectangle_area 함수 사용
# print(calcpkg.geometry.rectangle_area(30, 40))

from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))    # operation 모듈의 add 함수 사용
print(mul(10, 20))    # operation 모듈의 mul 함수 사용

print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용
