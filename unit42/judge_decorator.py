def html_tag(tag_type):
    def real_decorator(func):
        def wrapper():
            r = func()
            return f'<{tag_type}>{r}</{tag_type}>'
        return wrapper
    return real_decorator


a, b = input().split()


@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'


print(hello())
