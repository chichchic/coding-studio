fruits = {'orange', 'orange', 'cherry'}  # 중복을 허용하지 않음.
print(fruits)  # unordered한 자료형이라 출력시 매번 다른 결과를 보여줌.

# TODO: - 39장 반복 가능한 객체에서 설명이 나올듯 함.
# hash table로 만들어진 자료구조. 왜 출력시 매번 다른 결과를 보여주는걸까.

a = set(range(10))
print(a)
a |= {10}  # set.union 매서드와 동일
print(a)
a.update({11})
print(a)

b = frozenset(range(10))
print(b)
# b |= {10}
# b.update({11})
# frozenset은 사용 불가. 하지만 frozenset은 set안에 값으로 사용 가능
c = {b, b}
print(c)

a_set = {1, 2, 3, 4, 5}
a_subset = {1, 2, 4}
print(a_subset.issubset(a_set))  # True
print(a_subset < a_set)  # True
