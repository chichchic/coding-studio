def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
personal_info(*x)  # key값을 리스트로 전달


def personal_info2(**kwards):
    for kw, arg in kwards.items():
        print(f'{kw}: {arg}')


personal_info2(**x)
