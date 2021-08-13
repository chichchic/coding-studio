from collections import defaultdict

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(f'{key}: {value} ', end='')
print()

x.setdefault('e', 50)  # 이미 있는 key값을 변경할수는 없음
print(x)
x.update(a=11)  # key 값이 문자열일때만 사용 가능, update는 새로운 값 추가, 기존 값 변경 모두 사용 가능
print(x)

y = {1: 1, 2: 2, 3: 3}
print(y)
y.update({1: -1})
print(y)
y.update([[2, -2]])
print(y)
y.update(zip([1, 2], [10, 20]))
print(y)

z = {'a': 'a', 'b': 'b', 'c': 'c'}
print(z.items())
print(z.keys())
print(z.values())
print(z)
print(z.pop('a'))  # 'a' key가 가진 값을 반환하면서 삭제
print(z)
print(z.pop('z', 0))  # key 값이 없을 경우 에러를 발생시키지 않고 기본값을 반환한다.

del z['c']
print(z)

keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys)
print(my_dict)
my_dict2 = dict.fromkeys(keys, 100)
print(my_dict2)

default_dict = defaultdict(int)  # key가 존재하지 않더라도 에러를 발생시키지 않는다.
print(default_dict['c'])
# 기본값 생성 함수를 넣어주면 키 값이 존재하지 않을때 해당 값을 기본으로 가지는 dict을 반환해준다.
default_dict2 = defaultdict(lambda: 'default')
print(default_dict2['c'])

dict_comprehension = {key: value for key,
                      value in dict.fromkeys(range(4), 'empty').items()}
print(dict_comprehension)

dict_comprehension2 = {key: 0 for key in range(4)}
print(dict_comprehension2)
dict_comprehension3 = {key: 0 for key in range(4) if key != 2}
print(dict_comprehension3)
