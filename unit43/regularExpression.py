import re
r1 = re.match('Hello', 'Hello, world!')
r2 = re.match('Python', 'Hello, world!')
r3 = re.match('hello|world', 'elloollehello')  # 처음부터 일치해야지만 찾는다.
print(r1, r2, r3)
# 가장 처음 or 가장 끝 파악
r4 = re.search('^Hello', 'Hello, world!')
r5 = re.search('world!$', 'Hello, world!')
r6 = re.search('hello|world', 'elloollehello')  # 중간부터 일치해도 찾아준다.
print(r4, r5, r6)
p = re.compile('[0-9]+')  # 정규 표현식 패턴을 객체로 만들어서 사용
c1 = p.match('1234')
c2 = p.search('hello')
print(c1, c2)
m1 = re.match('([0-9]+) ([0-9]+)', '10 295')
print(m1.group())
print(m1.group(0))
print(m1.group(1))
print(m1.group(2))
m2 = re.match(
    '(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
print(m2)
f = re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')
print(f)

s1 = re.sub('apple|orange', 'fruit', 'apple box orange tree')
print(s1)


def multiple10(m):
    n = int(m.group())
    return str(n * 10)


s2 = re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz')
print(s2)

s3 = re.sub('[0-9]+', lambda m: str(int(m.group()) * 10),
            '1 2 Fizz 4 Buzz Fizz 7 8')
print(s3)

s4 = re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234')
print(s4)

s5 = re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})',
            '<\\2>\\3</\\2>', '{ "name": "james" }')
print(s5)

s6 = re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})',
            r'<\2>\3</\2>', '{ "name": "james" }')
print(s6)
