Hello = type('Hello', (), {})
print(Hello)


def replace(self, old, new):    # 클래스에 들어갈 메서드 정의
    while old in self:
        self[self.index(old)] = new


# list를 상속받음, 속성 desc, 메서드 replace 추가
AdvancedList = type('AdvancedList', (list, ), {
                    'desc': '향상된 리스트', 'replace': replace})

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)         # [100, 2, 3, 100, 2, 3, 100, 2, 3]
print(x.desc)    # 향상된 리스트


class MakeCalc(type):    # type을 상속받음
    def __new__(metacls, name, bases, namespace):      # 새 클래스를 만들 때 호출되는 메서드
        namespace['desc'] = '계산 클래스'              # 새 클래스에 속성 추가
        namespace['add'] = lambda self, a, b: a + b    # 새 클래스에 메서드 추가
        # type의 __new__ 호출
        return type.__new__(metacls, name, bases, namespace)


Calc = MakeCalc('Calc', (), {})    # 메타클래스 MakeCalc로 클래스 Calc 생성
c = Calc()                         # 클래스 Calc로 인스턴스 c 생성
print(c.desc)                      # '계산 클래스': 인스턴스 c의 속성 출력
print(c.add(1, 2))                 # 3: 인스턴스 c의 메서드 호출
