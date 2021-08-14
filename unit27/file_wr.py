file = open('./unit27/hello.txt', 'w')
file.write('Hello, world!')
file.close()

# hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
file = open('./unit27/hello.txt', 'r')
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기

with open('./unit27/hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)
