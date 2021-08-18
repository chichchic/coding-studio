class Calc:
    @staticmethod  # 인스턴스 속성에 접근이 불가능 함. 따라서 인스턴스 상태를 변화시키지 않는 순수함수를 만들때 사용한다.
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출
