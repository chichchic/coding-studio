# bytes는 요소의 내용을 변경할 수 없다.

b1 = bytes(10)
print(b1)
b2 = bytes(b'hello')
print(b2)

# bytearray는 요소의 내용을 변경할 수 있다.
x = bytearray(b'hello')
x[0] = ord('a')  # 문자 변경시 ord를 사용
print(x)

encode1 = '안녕'.encode()
encode2 = '안녕'.encode('euc-kr')
encode3 = '안녕'.encode('utf-8')
print(encode1)
print(encode2)
print(encode3)

print(encode1.decode())
print(encode2.decode('euc-kr'))
print(encode3.decode('utf-8'))
