class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 비공개

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))


maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()
maria.temp = 'temp'  # 생성 이후에도속성을 추가할 수 있음
print(maria.temp)
# print(maria.__wallet) # 출력 불가


class Person2:
    __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)


james = Person2()
# james.temp = 'temp'  # 생성 불가
