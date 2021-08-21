def find(str):
    result = None
    while True:
        line = yield result
        result = str in line


f = find('Python')
next(f)

print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))

f.close()
