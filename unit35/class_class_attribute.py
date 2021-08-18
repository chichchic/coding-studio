class Person:
    bag = []  # 모든 인스턴스에서 속성을 공유한다.

    def put_bag(self, stuff):
        Person.bag.append(stuff)  # self를 사용하는것보다 명확한 표현


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)


class Person2:
    '''사람 클래스입니다.'''
    __item_limit = 10

    def __init__(self) -> None:
        self.bag = []  # 인스턴스 속성

    def put_bag(self, stuff):
        '''10개까지 리스트에 stuff를 넣을 수 있습니다.'''
        if Person2.__item_limit > len(self.bag):
            self.bag.append(stuff)
        else:
            print("bag overflow")


james = Person2()
james.put_bag('책')

maria = Person2()
maria.put_bag('1')
maria.put_bag('2')
maria.put_bag('3')
maria.put_bag('4')
maria.put_bag('5')
maria.put_bag('6')
maria.put_bag('7')
maria.put_bag('8')
maria.put_bag('9')
maria.put_bag('10')
maria.put_bag('11')

print(james.bag)
print(maria.bag)

print(Person2.__doc__)
